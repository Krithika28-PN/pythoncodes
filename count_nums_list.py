
s = 'krithika'

count = {}#use dictionary

for num in s:
    if num in count:
        count[num] += 1  #adding in the dict not in number
    else:
        count[num] = 1

print(count)











