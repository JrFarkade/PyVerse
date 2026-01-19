# Currency Converter
print("Currency Converter")

rates = {
    "USD": 1.0,
    "INR": 90.81,
    "EUR": 0.86,
    "GBP": 0.74,
    "JPY": 158.0
}

amount = float(input("Enter amount: "))
from_currency = input("From currency (USD/INR/EUR/GBP/JPY): ").upper()
to_currency = input("To currency (USD/INR/EUR/GBP/JPY): ").upper()

if from_currency in rates and to_currency in rates:
    usd_amount = amount / rates[from_currency]
    converted = usd_amount * rates[to_currency]
    print(f"\n{amount} {from_currency} = {converted:.2f} {to_currency}")
else:
    print("\nInvalid currency code!")
