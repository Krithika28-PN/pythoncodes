s = 'My name is Rohit'

words = s.split()
# to join back use below syntax
# joined = ' '.join(words)
max_length = words[0]

for word in words:
    if len(max_length) < len(word):
        max_length = word
print(max_length)

str = str(words)
print(str)
# print(words[::-1])
