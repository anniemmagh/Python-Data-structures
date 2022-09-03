# List -data structure
x = 1
myList = [1,2,3,4]
print(myList)

# allows differtent data types
# mmylist =[1,2,"Ani","Megi", True,False, 3.0]
# name = mmylist[3] 
# print(name)

# #changeable - List-ის თვისება
# # List allows Duplicates
# mmylist[1] = 1
# print(mmylist)
# n = len(mmylist)
# print(mmylist[n-1]) # Get last data
# print(mmylist[len(mmylist)-1]) # Get last data

# print(mmylist)
# print(len(mmylist)) 

# add datas in the list
newList =[1,2,"Ani","Megi", True,False, 3.0, 10,1000,"Maghlakvelidze", "Georgia"]
newList.append("Tbilisi") # add item
newList.pop(5)  # delete item
newList.remove("Georgia") # Remove item
print(newList)

# set - data structure
mySet = {1,2,"Ani","asus",1} # duplicates gonna delete
print(mySet)