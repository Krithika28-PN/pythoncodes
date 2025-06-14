lst = [1, 2, 3, 4, 5]
k = 7
k = k % len(lst)  # this helps when k > length of list its gives k as remainder value
list2 = lst[k:] + lst[:k]  # lst[2:] = [3, 4, 5] + lst[:2] = [1, 2]

print(list2)