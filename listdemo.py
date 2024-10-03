# list can store multiple data, data can be of different types od data like int, str, float
# list can store the duplicate data
# list is an ordered data set - sorting (Ascending or descending)

# create list and store friends name
friendlist = ['Anjali','Nitiyansh', 'Tripti', 'Shreya']

# print the list of friends name
print(friendlist)

# add the age of your friend into list
friendlist.append(18)         # append will add the data into the end of the list
friendlist.append(20)
friendlist.append(19)
friendlist.append(20)
print(friendlist)

# Add the data into list using index no.
friendlist.insert(0,"Nityansh")
print(friendlist)

#To access the data using index no.
print(friendlist[0])

# Access the complete list
for name in friendlist:
    print(name)

# To remove data
friendlist.remove("Nityansh")     # remove - removes data using value
print(friendlist)

friendlist.pop(4)
print(friendlist)               # pop - removes data using index no.

# Stack - FILO, Queue - FIFO



#Add the 5 fav city name in the list
#Add my fav city name kasol in first index
#remove the last city name from list - using pop
#sorting the list data
 #friendlist.sort()
#print the list data

placelist =["Shimla","Dehradun","Chandigarh","Haryana","noida"]
placelist.insert(0,"kasol")
placelist.pop(4)
placelist.sort()
print(placelist)
