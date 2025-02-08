def invest(amount, rate, years):
    for years in range(0, years):
        amount = amount * (1 + rate)
        print(f"year {years}: {amount:.2f}")

amount = float(input("Enter your principal amount: "))
years = int(input("How long do you wish to invest it?  "))
rate = float(input("At what rate do you wish to invest it? "))
invest(amount, rate, years)