# map(function, iterable)

numbers = ["1", "2", "3", "4"]
result = list(map(int, numbers))  # Convert each string to an integer
print(result)

list = [int(i) for i in numbers]
print(list)

