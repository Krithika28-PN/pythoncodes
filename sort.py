list = [23,53,90,868,12]

n = len(list)

for i in range(n):
    for j in range(i+1,n):
        if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]
print(list)



