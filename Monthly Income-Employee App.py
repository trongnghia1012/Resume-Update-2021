h = int(input("Enter number of hours worked: "))
regular_rate = 10
overtime_rate = regular_rate *1.5
regular_pay = 40 * regular_rate
overtime_pay = (h-40)*(regular_rate*overtime_rate)
gross_pay = regular_pay + overtime_pay
w = (gross_pay*0.1) + (gross_pay*0.06)
net_pay = gross_pay - w
monthly_inc= net_pay*4

print("Here is your paycheck post-taxes: $", net_pay)
print("Here is your monthly income post-taxes: $",monthly_inc)

