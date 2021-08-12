'''
term = total months
rate = monthly interest
loan = total loan value

Calculate the monthly interest rate

'''

months = int(input("Enter Mortgage Term (in months): "))
rate = float(input("Enter interest rate: "))
loan = float(input("Enter loan value: "))

years = months / 12

monthly_rate = rate / 100 / 12
print(monthly_rate)

x = (1 + monthly_rate)**(-months)
print(x)

payment = (monthly_rate / (1 - (1 + monthly_rate)**(-months))) * loan
print(payment)

print(f"Monthly payment for a ${loan} and {years} year mortgage at {rate} interest rate is: {payment}".format(loan, years, rate, payment))
