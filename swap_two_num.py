# Write a Python program to swap two numbers without using a temporary variable.
list = [1,2,3,4,5]

list[0],list[4] = list[4],list[0]
print(list)