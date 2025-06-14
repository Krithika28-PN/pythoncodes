# count the freq of words in the sentence
s = 'Sheena loves eating apple and mango, her sister also loves eating apple and mango'
print(s)
s = s.split()
print(s)
count = {}
for word in s:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print(count)