# Typecasting in Python :- Convert one data type to another data type
# e.g. - sometime when we purchase iten in float we paid in integer

PurchaseIP= 90
PaidIP=int(PurchaseIP)
print("Paid amount is: ",PaidIP)

# Add scholorship of 25000 in fee
clgFee=input("Enter your college fee: ")
clgFee=int(clgFee)
# or we can do this:- clgFee=int(input("Enter your college fee: "))
print("After scholorship: ",clgFee - 25000)

# Find the age in years when born year and current year are given by user
BornYear=int(input("Enter your born year: "))
CurrentYear=int(input("Enter your current year: "))
print("Your age is: ", CurrentYear - BornYear, "years")