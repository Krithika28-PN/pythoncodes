s = 'My name is Rohit'
s2 = []
word = ''

for char in s:

    if char != ' ':
        word = word + char
    elif char == ' ':
        s2.append(word)
        word = ''
s2.append(word)#for last word
s2 = ' '.join(s2)# to convert from list to string
print(s2)