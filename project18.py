import os
import secrets
from datetime import datetime, timedelta, timezone
from typing import List
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from passlib.context import CryptContext
import jwt

# configuration constants
SECRET_KEY = os.getenv("PROJECT18_SECRET_KEY") or secrets.token_urlsafe(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# initialize security contexts
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
app = FastAPI(title="Secure RBAC REST API")

# mock database simulating users with defined roles
USER_DB = {
    "alice": {
        "username": "alice",
        "hashed_password": pwd_context.hash("admin123"),
        "roles": ["admin", "user"]
    },
    "bob": {
        "username": "bob",
        "hashed_password": pwd_context.hash("user123"),
        "roles": ["user"]
    }
}

# pydantic schemas for data validation 
class Token(BaseModel):
    access_token: str
    token_type: str

class UserSchema(BaseModel):
    username: str
    roles: List[str]

# help functions for authentication and token mechanics
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme)) -> UserSchema:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        roles: List[str] = payload.get("roles", [])
        if username is None:
            raise credentials_exception
        return UserSchema(username=username, roles=roles)
    except jwt.InvalidTokenError:
        raise credentials_exception
    
# RBAC Dependency Class
class Rolechecker:
    def __init__(self, allowed_roles: List[str]):
        self.allowed_roles = allowed_roles

    def __call__(self, current_user: UserSchema = Depends(get_current_user)):
        # check if the user has at atleast one of the allowed roles
        if not any(role in current_user.roles for role in self.allowed_roles):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have the required permissions to access this resource"
            )
        return current_user
    
# API Endpoints
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = USER_DB.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )    
    # Embed roles directly inside the JWT payload for stateless authorization
    access_token = create_access_token(
        data={"sub": user["username"], "roles": user["roles"]}
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/public")
async def public_endpoint():
    return {"message": "Welcome! Anyone can see this endpoint."}

@app.get("/dashboard")
async def user_dashboard(current_user: UserSchema = Depends(Rolechecker(["user", "admin"]))):
    return {"message": f"Hello {current_user.username}, welcometo your dasboard."}

@app.get("/admin-panel")
async def admin_panel(current_user: UserSchema = Depends(Rolechecker(["admin"]))):
    return {"message": f"Access granted to admin panel. Welcome, Admin {current_user.username}."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
            
           
