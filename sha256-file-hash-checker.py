import hashlib

def calculate_hash(filename):
    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:
        while True:
            chunk = file.read(4096)

            if not chunk:
                break

            sha256.update(chunk)

    return sha256.hexdigest()

filename = input("Enter file name: ")

file_hash = calculate_hash(filename)

print("\nSHA_256 HASH:")
print(file_hash)