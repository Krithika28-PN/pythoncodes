s = "abcd"
output = []
temp = ""

for char in s:
    temp += char  # Add one character at a time
    output.append(temp)

print(output)
# output = ['a', 'ab', 'abc', 'abcd']