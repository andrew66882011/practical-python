# mortgage.py
#
# Exercise 1.7
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = int(input('extra payment is '))
extra_payment_start_month = int(input('extra payment start month is '))
extra_payment_end_month = int(input('extra payment end month is '))
total_paid = 0.0
month = 0

while principal > 0:
    month+=1
    if (month <= extra_payment_end_month) and (month >= extra_payment_start_month) :
        principal = principal * (1 + rate/12) - (payment+extra_payment)
        total_paid = total_paid + (payment+extra_payment)
        print(month, round(total_paid, 2), round(principal, 2))
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
        print(month, round(total_paid, 2), round(principal,2))

print('Total paid', round(total_paid, 2))
print('Months', month)
