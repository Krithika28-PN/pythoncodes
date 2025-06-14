s = "Python is a good language"

vowels = "aeiouAEIOU"
word = ''
for char in s:
    if char not in vowels:
        word = word + char
print(word)
# list1 = list(word)
# print(list1)