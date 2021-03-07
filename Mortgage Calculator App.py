### Mortgage Calculator App ###

print("|~~~~~~~~~~Mortgage Calculator App~~~~~~~~~|")
print('\n')
interest =(float(input('Enter your present loan interest rate: %'))/100)/12
years =float(input('Enter the term of loan (years): '))*12
amount =float(input('Enter the amount of loan after put down-payment: $'))

numerator = interest*((1+interest)**years)
denominator = (1+interest)**years-1

f = float("{0:.2f}".format(amount*numerator/denominator))
  
print('\n')
print("Principal Borrowed:%7.2f"% amount)
print("Monthly Mortgage Payment: $",f)


print("\nThank you for using the app ^.^")
