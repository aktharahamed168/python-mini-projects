from datetime import datetime

print("===== Age Calculator =====")

dob = input("Enter your Date of Birth (DD-MM-YYYY): ")

birth_date = datetime.strptime(dob, "%d-%m-%Y")

today = datetime.today()

age = today.year - birth_date.year

if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

print(f"\nYou are {age} years old.")
