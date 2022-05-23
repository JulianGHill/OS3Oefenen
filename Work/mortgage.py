# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
MonthsExtraPayment = 12
months = 1
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    # if MonthsExtraPayment > 0:
    #     principal = principal * (1+rate/12) - (payment+extra_payment)
    #     total_paid = total_paid + (payment+extra_payment)
    #     MonthsExtraPayment = MonthsExtraPayment - 1
    # else:
    #     principal = principal * (1+rate/12) - payment
    #     total_paid = total_paid + payment

    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        principal = principal * (1+rate/12) - (payment+extra_payment)
        total_paid = total_paid + (payment+extra_payment)
        print(months, ' ', total_paid, ' ', principal)
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
        print(months, ' ', total_paid, ' ', principal)

    months = months + 1
        
print('Total paid', total_paid)
print('Total months', months)
