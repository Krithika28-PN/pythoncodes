ip = '175.64.88.4'

s = ip.split('.') # new functionality in split
print(s)
count = 0
for num in s:
    count = count + int(num) # We need to convert the nums from str to int first

print(count)