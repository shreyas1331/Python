friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(friends)
friends.append("Harry")
print(friends)

l1 = [1, 34,62, 2, 6, 11]
# l1.sort()
# l1.reverse()
# l1.insert(2, 333333) # Insert 333333 such that its index in the list is 3
value = l1.pop(3)
print(value)
print(l1)



# ----------------------------------------------
# nested list comprehsion
list1=['a','b','c','d']
list2=[1,2,3,4,5,6]

pair=[[i,j] for i in list1 for j in list2]

print(pair)

##list comprehension with function calls
words=['shreyas','mahajan','hello']

length=[len(word) for word in words]
print (length)