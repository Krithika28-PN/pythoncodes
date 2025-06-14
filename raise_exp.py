list = [5,7,45,23,1,5]

for i in list:
    if i == 1:
        raise Exception("Exception: found 1")
    else:
        print(i)