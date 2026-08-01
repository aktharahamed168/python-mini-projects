import requests

print("===== URL Shortener =====")

long_url = input("Enter Long URL: ")

url = "https://cleanuri.com/api/v1/shorten"

response = requests.post(url, data={"url": long_url})

if response.status_code == 200:
    data = response.json()
    print("\nShort URL:")
    print(data["result_url"])
else:
    print("Failed to shorten the URL.")
