list1 = ["India","Is","My","Country"]
list2 = []
n = len(list1)
for i in list1:
    for j in i:
        if j == 'I':
            list2.append(i)

print(list2)