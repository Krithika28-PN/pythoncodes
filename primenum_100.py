# 1 - 100 prime numbers list
n = 100
prime_num_list = []
for i in range(1,n):
    count = 0
    for j in range(1,i+1):  # checks division of number till the current i number
        if i % j == 0:
            count += 1
    if count <= 2:
        prime_num_list.append(i)
print(prime_num_list)