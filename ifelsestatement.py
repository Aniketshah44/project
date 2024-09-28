#conditional statement will check condition is true or not
#to check the condition we use if else

#WAP to check user eligible for voting
userAge=int(input("Enter your age: "))
#note the default input function return type is string
# for vote the age must be greater than 18
if userAge  > 18:
     print("you're elligible for voting")
else:
     print("you're not elligible for voting")

#to check user is male or female
gen=input("enter your gender:")
if gen == "M":
       print("u are not elligible to sit in first compartment of metro")
elif gen == "F":
       print("you are elligible to sit in first compartment of metro")
else:
     print("You can sit in any compartment")    

#WAP if gender is male and age is greater than 18 -> govt job apply
# else female and age is greater than 18 -> private job apply        
 
gender=input("Enter your gender: ")
age=int(input("Enter your age: "))
if age > 18: 
   if gender == "Male": 
     print("You can apply for govt job")
   elif gender == "female":
     print("You can apply for private job")
   else:
     print("Sorry there is no opening")  
else:
  print("You are under age")   
   