import requests

print("===== Currency Converter =====")

amount = float(input("Enter Amount: "))
from_currency = input("From Currency (e.g. USD): ").upper()
to_currency = input("To Currency (e.g. INR): ").upper()

url = f"https://open.er-api.com/v6/latest/{from_currency}"

response = requests.get(url)
data = response.json()

if data["result"] == "success":
    rate = data["rates"].get(to_currency)

    if rate:
        converted = amount * rate
        print(f"\n{amount} {from_currency} = {converted:.2f} {to_currency}")
    else:
        print("Invalid target currency code.")
else:
    print("Invalid source currency code.")
