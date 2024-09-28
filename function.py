# function can perfrom any task
# it can be reuse, function will return the result

# create function to print name
def printname():
    print("My name is Aniket")

#call function to print the name
printname()

# create function to concatenate fname and lname
fname=input("Enter first name: ")
lname=input("Enter last name: ")
def printFullNmae(firstname, lastname):
    print(firstname+ " "+ lastname) 
printFullNmae(fname, lname)    


# create function to find area of square
side=int(input("Enter side: "))
ar=side*side
def area(a):
    print("area = ",a)
area(ar)