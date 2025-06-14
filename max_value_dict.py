# How would you find the key with the maximum value in a dictionary?
dict1 = {'a': 10, 'b': 35, 'c': 55, 'd': 40}
n = len(dict1)
max_value = 0
for char in dict1.values():
    if char > max_value:
        max_value = char
print(max_value)
for i in dict1:
    if dict1[i] == max_value:
        print(i)