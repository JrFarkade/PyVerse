# Unit Converter
print("UNIT CONVERTER")

units = {
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
    "inch": 0.0254,
    "ft": 0.3048,
    "mile": 1609.34
}

print("\nAvailable units: cm, m, km, inch, ft, mile")

value = float(input("Enter value: "))
from_unit = input("From unit: ").lower()
to_unit = input("To unit: ").lower()

if from_unit in units and to_unit in units:
    meters = value * units[from_unit]      # convert to meters
    result = meters / units[to_unit]       # convert meters to target unit
    print(f"\n{value} {from_unit} = {result:.4f} {to_unit}")
else:
    print("\nInvalid unit entered!")
