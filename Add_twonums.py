#addition of two number should be equal to given number
sum = 10
list = [1,4,5,6,3,7]
n = len(list)
for i in range(n):
    for j in range(i + 1, n):
        if (list[i] + list [j] == sum):
            print(f"this numbers gives the result {list[i]},{list[j]}")


