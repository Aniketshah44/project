#while loop is used to peerform iteration
#until condition is false

#print the no. from 1 to 10
x = 1
while x < 11:
    print(x)
    x = x + 1   

for i in range(1,5):
    print("_")    

#print no. 10 to 1
n = 10
while n > 0:
    print(n)
    n = n - 1    

#print table no
no = int(input("Enter no. for table: "))
a = 1
while a < 11:
    print(a * no)    
   # a = a + 1
    a+=1           # += also means a = a + 1

#print reverse table
n = int(input("Enter no. for table: "))
a = 10
while a > 0:
    print(a * n)
    a -= 1
        
#print reverse table till 5
t = int(input("Enter no. for table: "))
a = 10
while a > 4:
    print(a * t)
    a -= 1

# print the pattern 1 4 7 10 13 16
b = 1
while b < 17:
    print(b)
    b+=3 

#print this pattern 21 16 11 6 1
c = 21
while c >= 1:
    print(c)
    c-=5  

# print the pattern 1 7 19 25
d=1
while d < 26:
    if d!=13:
       print(d)
    d+=6