list = [2,4,7,2,5,34,6,5,8,3,4]

list2 = []
n = len(list)
for i in list:
    if i not in list2:
        list2.append(i)
print(list2)

# different method

# removing repeated numbers
# first we made a dict with count of each numbers
# then we added the numbers with only 1 count in an empty list2 and then print list2

list = [2,4,7,2,5,34,6,5,8,3,4]
n = len(list)
count = {}
list2 = []
for i in list:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)
for i in count:
    if count[i] == 1:
        list2.append(i)
print(list2)



