my_dict = {'a': 1, 'b': 2, 'c': 3}

my_dict['d'] = 4
print(my_dict)
for key in my_dict.keys():# keys() for only keys and values() for only values
    print(key)
for values in my_dict.values():# keys() for only keys and values() for only values
    print(values)
for i in my_dict.items():# keys() for only keys and values() for only values
    print(i)