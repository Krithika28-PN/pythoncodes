class Employee:
 def __init__(self, fname, lname, age):
    self.fname = fname
    self.lname = lname
    self.age = age

e1 = Employee("steve", "jobs", 26)
e2 = Employee("bill", "gates", 27)
e3 = Employee("amy", "masters", 28)
e4 = Employee("john", "dow", 22)

employees = [e1, e2, e3, e4]

sorted_list = sorted(employees,key=lambda x: x.age)
print(sorted_list)

# numbers = [4, 2, 8, 1, 5]
#
# # Using sort() - modifies the original list
# numbers.sort()
# print(numbers)  # [1, 2, 4, 5, 8]
#
# # Using sorted() - returns a new sorted list
# numbers = [4, 2, 8, 1, 5]
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)  # [1, 2, 4, 5, 8]
#
# numbers = [4, 2, 8, 1, 5]
#
# # Using sort() with reverse=True
# numbers.sort(reverse=True)
# print(numbers)  # [8, 5, 4, 2, 1]
#
# # Using sorted() with reverse=True
# sorted_numbers = sorted(numbers, reverse=True)
# print(sorted_numbers)  # [8, 5, 4, 2, 1]
#
# words = ["apple", "banana", "cherry", "date"]
#
# # Sort alphabetically
# print(sorted(words))  # ['apple', 'banana', 'cherry', 'date']
#
# # Sort by length
# print(sorted(words, key=len))  # ['date', 'apple', 'banana', 'cherry']
#
#
# my_dict = {'b': 3, 'a': 5, 'c': 1}
#
# # Sort by keys
# print(sorted(my_dict))  # ['a', 'b', 'c']
#
# # Sort by values
# print(sorted(my_dict.items(), key=lambda x: x[1]))  # [('c', 1), ('b', 3), ('a', 5)]
