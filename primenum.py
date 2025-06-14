
def prime_num(num):
    # n = 100
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1
    if count <= 2:
        print("Prime number")
    else:
        print("Not prime")

prime_num(79)