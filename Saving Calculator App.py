### Saving Calculateion App ###


print("|~~~~~~~~~~Future Calculation Saving~~~~~~~~~|")
print('\n')
p=float(input('Enter your present value of the account: $'))
i=float(input('Enter the monthly interest rate: '))/100
t=int(input('Enter number of months: '))
f= p*(1+i)**t

print('\nAftet', t, 'months,',"your saving account will accumulate up to ${:.2f}".format(f))
print("\nThank you for using the app ^.^")
