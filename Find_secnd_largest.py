# Find the second large number in a list.

list = [2,4,6,2,7,3,56,54,2,66,2,4,23,68,57]

n = len(list)

for i in range(n):
    for j in range(i+1, n):
        if list[i] < list[j]:
            list[i],list[j] = list[j],list[i]

print(list[1])
