def list_dictionary(names,numbers):
    list_dict = {}
    for word, number in zip(names, numbers):
        list_dict[word] = number
    print(list_dict)

s = ["Rohit", "Prem", "Samarth"]
num = [342,454,686]
list_dictionary(s,num)