# # List -data structure
# x = 1
# myList = [1,2,3,4]
# print(myList)

# # allows differtent data types
# # mmylist =[1,2,"Ani","Megi", True,False, 3.0]
# # name = mmylist[3] 
# # print(name)

# # #changeable - List-ის თვისება
# # # List allows Duplicates
# # mmylist[1] = 1
# # print(mmylist)
# # n = len(mmylist)
# # print(mmylist[n-1]) # Get last data
# # print(mmylist[len(mmylist)-1]) # Get last data

# # print(mmylist)
# # print(len(mmylist)) 

# # add datas in the list
# # newList =[1,2,"Ani","Megi", True,False, 3.0, 10,1000,"Maghlakvelidze", "Georgia"]
# # newList.append("Tbilisi") # add item
# # newList.pop(5)  # delete item
# # newList.remove("Georgia") # Remove item
# # print(newList)

# # set - data structure
# mySet = {1,2,"Ani","asus",1} # duplicates gonna delete
# # names = ["Marta" , "Giorgi" ,"Ani", "Marta"]
# # names_set = set(names)
# # print(names_set)
# mySet.add(120)
# mySet.remove("Ani")

# print(mySet)
# numbers = {1,10,100}
# nnames = {"Ani", "Marta" , "Giorgi"}
# numbers_names = numbers.union(nnames)
# numbers.update(nnames)
# print(numbers_names)


# tuple
#allows different data types & duplicate 
# ordered and unchangeable 
# myTuple = (1,2, "Test 1" , True,2,1)
# mylist = list(myTuple)

# print(mylist) # change tuple as a list
# myTuple = (1,2, "Test 1" , True,2,1)
# mylist = list(myTuple)
# mylist[2] = "matlab"
# mylist.append(10)
# myTuple = tuple(mylist) # list to tuple
# print(myTuple)
# myTuple = (1,2, "Test 1" , True,2,1)
# mylist = list(myTuple)
# mylist[2] = "matlab"
# mylist.append(10)
# newTuple = (12, "python" , "ES6","HTMl5")
# tupleaddition = myTuple + newTuple
# print(tupleaddition)

myTuple = (1,2, "Test 1" , True,2,1)
mylist = list(myTuple)
mylist[2] = "matlab"
mylist.append(10)
newTuple = (12, "ES6","HTMl5")
tupleaddition = myTuple + newTuple
print(myTuple.index("Test 1")) # find element index in tuple

# Dictionary - data structure
#ordered , changeable , doesnt allows duplicates
# key: value
# cars = {"Brand":"Ford" , 
#         "Model": " Mustang" ,
#         "year" : 1964,
#  }
# print(type(cars)) 
# cars = {"Brand":"Ford" , 
#         "Model": " Mustang" ,
#         "year" : 1964,
#  }
# cars["Color"] = "Purple"
# print(cars) #add key to dictionary
# cars = {"Brand":"Ford" , 
#         "Model": " Mustang" ,
#         "year" : 1964,
#  }
# cars.update({"color": "purple"})
# print(cars)
cars = {"Brand":"Ford" , 
        "Model": " Mustang" ,
        "year" : 1964,
 }
cars.update({"color": "purple"})
print(cars.get("Model"))
