my_dictionay= {6: 8, 7: 10}

print("Add elements to dictionary:")
my_dictionay[1] = 3
my_dictionay[2] = 7
my_dictionay[3] = 8
my_dictionay[4] = 9
my_dictionay[5] = 0


print("Dictionary elements:", my_dictionay)

# pop or delete elements from dictionary:

# pop returns the value of the key popped
poppedElement = my_dictionay.pop(5)

print("\nmy_dictionay.pop(5): ", poppedElement)

# deletes the element from the dictionary and doesnt have any return value
del my_dictionay[4]
print("Dictionary elements on using del my_dictionay[4]:", my_dictionay)

# popitem() removes random/ arbitrary key value from the dictionary in the form of tuple
element = my_dictionay.popitem()
print("my_dictionay.popitem():", element[0], element[1])

print("\nDictionary after operations: ", my_dictionay)

print("\nkeys in dictionary: my_dictionay.keys(): ", my_dictionay.keys())
print("values in dictionary: my_dictionay.values(): ", my_dictionay.values())

# check if a key/value is present in the dictionary
if 1 in my_dictionay.keys():
    print("key is present in the dictionary")
# copy of  dictionary:
dict_copy = my_dictionay.copy()


print("\nlooping over all the items of dict")
for key, value in dict_copy.items():
    print(key, value)

print("\nlooping over all the keys/values of dict")
for key in dict_copy.keys():
    print(key)


