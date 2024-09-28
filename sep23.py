name="Aniket"
email="aniket202006@gmail.com"
salary=25000
age=18
gender= "Male"

#To print variable in string statement

# Solution -1
print("My name is "+name+ "my age is ",age,"my gender is "+gender)
# Solution -2 
print(f"My name is {name} and email is {email} and my salary is {salary}")  #using filt f
# Solution -3 
ageInString=str(age)
print("My name is "+name+ " my age is "+ageInString+" my gender is "+gender)  #using typecasting

# Typecasting in Python :- Convert one data type to another data type
# e.g. - sometime when we purchase iten in float we paid in integer

PurchaseIP= 90
PaidIP=int(PurchaseIP)
print("Paid amount is: ",PaidIP)

#To get input from user
clgname=input("Enter your college name:")
clgFee=input("Enter your college fee: ")
print("My clg name is "+clgname+ " fees is "+clgFee)

# Add scholorship of 25000 in fee
clgFee=int(clgFee)
# or we can do this:- clgFee=int(input("Enter your college fee: "))
print("After scholorship: ",clgFee - 25000)

# Find the age in years when born year and current year are given by user
BornYear=int(input("Enter your born year: "))
CurrentYear=int(input("Enter your current year: "))
print("Your age is: ", CurrentYear - BornYear, "years")

print(type(name))
print(type(age))