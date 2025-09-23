TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
tariff = int(input("Which tariff? 11 or 31: "))
if tariff == 11:
    price_per_kWh = TARIFF_11
elif tariff == 31:
    price_per_kWh = TARIFF_31
else:
    print("Neither option chosen. Requesting input")
    price_per_kWh = float(input("Enter cents per kWh: ")) / 100
daily_use_kWh = float(input("Enter daily use in kWh: "))
number_of_days = int(input("Enter number of billing days: "))
estimated_bill = price_per_kWh * daily_use_kWh * number_of_days
print(f"Estimated bill: ${estimated_bill:.2f}")
