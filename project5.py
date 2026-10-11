import requests

ip = input("Enter an IP address: ")

url = f"http://ip-api.com/json/{ip}"

response = requests.get(url)
data = response.json()

print("\nIP Information")
print("IP:", data["query"])
print("Country:", data["country"])
print("Region:", data["regionName"])
print("City:", data["city"])
print("ISP:", data["isp"])