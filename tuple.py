# Tuple - is collection of list
#tuple uses less memory and faster than list
# in list we can use dynamic datatype but not with tuple
my_tuple = (1,2,3,4,5)
#my_tuple[3] = 64 #Tuple is immutable in nature unlike List
print(my_tuple)

# To convert tuple to list

my_list = list(my_tuple)
print(my_list)

# To convert list to tuple

tuple = tuple(my_list)
print(tuple)

#tuple within tuple
hero1 = ("batman", "bruce")
hero2 = ("wonder women", "shaktiman")
newtuple = (hero1,hero2)
print(newtuple)
print(newtuple[0][1])

# to search in tuple
print("batman" in hero1)

#To add element in tuple
t = (12, 4,6,7)
t2 = (8,)#comma is important
t1 = t + t2
print(t1)
