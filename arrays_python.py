# Create an array in python
new_array = [1, 2, 3, 4, 5, 6, 3]

# add a new element to the array:
new_array.append(45)
print("Added a new # to the array: ", new_array)

print("Access element of an array using index: ", new_array[4])

#print("Access the element with index out of array gives list index out of range: ", new_array[56])

print("Access elements using negative indexing.", new_array[-1], new_array[-2])

#print("Access elements out of range using negative indexing: gives index out of range error", new_array[-34])

print("Find length of the array: ", len(new_array))

#pop returns the poped element
print("Remove element from an array using pop() without index removed the last element", new_array.pop())

print("Remove element from an array using pop(1) removes the element from the index 1: ", new_array.pop(1))

# remove() doesn't return the removed element. Its return type is None
print("Remove element from an array using remove(3): this removes the first occurance of the mentioned element", new_array.remove(3))
print(new_array)

# also delete an element
del new_array[1]
print("Remove element using del ")
print("Array after deleting the element: ", new_array)

# Concatenate arrays using + :
# List/Array can have data of different types:
a_new_array = [0, 9, 8]
b_new_array = ['3', '5']
new_array += a_new_array + b_new_array
print("new Concatenated array: ", new_array)

# Repeat elements using *:
a_new_array = a_new_array * 2
print("Repeat elements using * : ", a_new_array)

# Create a copy of an array:
new_array_copy = new_array.copy()
print("Create a copy of an array using .copy(): ", new_array_copy)

#Slicing the array:
print("Slicing: ")
print("new_array_copy[1:4]; Doesn't include 4 when slicing", new_array_copy[1:4])
print("new_array_copy[:3]", new_array_copy[:3])
print("new_array_copy[-4:]", new_array_copy[-4:])
print("new_array_copy[-3:-1]", new_array_copy[-3:-1])
print("new_array_copy[-3:-3]", new_array_copy[-3:-3])

#different operations:
new_array.extend([34, 23])
print("new_array.extend([34,23]): ", new_array)
new_array.append([34, 23])
print("new_array.append([34,23]): ", new_array)
new_array.insert(0, 12)
print("new_array.insert(0, 12): ", new_array)
a_new_array.sort()
print("a_new_array.sort(): ", a_new_array)
new_array.reverse()
print("new_array_copy.reverse(): ", new_array)
