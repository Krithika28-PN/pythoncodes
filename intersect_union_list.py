# Find the intersection and union of two lists.

list1 = [1, 2, 3, 4, 5,5]
list2 = [4, 5, 6, 7, 8,4]
list = []
for i in list1:  # int in list1
    if i in list2:  # check int of list1 in list2
        if i not in list:  # checks common int already present in intersection list
            list.append(i)  # if not then append in the list
print(list)
