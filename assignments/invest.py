def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount = amount * (1 + rate)
        print(f"year {year}: ${amount:.2f}")

print("Enter the amount to invest: ")
amount = float(input())

print("Enter the annual rate (as a decimal): ")
rate = float(input())

print("Enter the number of years: ")
years = int(input())

invest(amount, rate, years)