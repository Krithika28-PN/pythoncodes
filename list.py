my_list = [1,2,3,4]

# to add single element in the list
my_list.append(5)
my_list.append(6)
print(my_list)

# to add multiple elements in the list at once
my_list.extend([5,6,7,8])
print(my_list)

# to insert element in specific place in list
my_list.insert(1,"Banik") #(index,Value)
print(my_list)
my_list.insert(-1,"Banik") #(index,Value)
print(my_list)

# to remove any element
my_list.remove("Banik")
print(my_list)
my_list.remove("Banik")

print(my_list)

# to sort the list in ascending odr
my_list.sort()
print(my_list)

# to sort the list in decending odr
my_list.reverse()
print(my_list)