my_dict = {'apple': 3, 'banana': 2, 'cherry': 5}
dict2 = dict(sorted(my_dict.items(),key= lambda x: x[1],reverse=True))
print(dict2)