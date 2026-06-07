list1=list(map(str,input("enter the input: ").split()))
print(list1)
print(list1.pop(0))
print(list1)
list1.append('llll')
print(list1)
list1.insert(2,'lolpotato')
print(list1)
print(len(list1))
# Method	Description
# append(x)	Adds an item to the end of the list
# extend(iterable)	Adds all elements of an iterable to the list
# insert(i, x)	Inserts an item at a specified position
# remove(x)	Removes the first occurrence of a value
# pop([i])	Removes and returns item at index i (last item if omitted)
# clear()	Removes all items from the list
# index(x[, start[, end]])	Returns the index of the first occurrence of a value
# count(x)	Returns the number of occurrences of a value
# sort(key=None, reverse=False)	Sorts the list in place
# reverse()	Reverses the elements of the list
# copy()	Returns a shallow copy of the list