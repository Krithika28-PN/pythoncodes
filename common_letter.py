s1 = 'NAINA'
s2 = 'REENE'
common_letters = []
for char in s1:
    if char in s2:
        if char not in common_letters:
            common_letters.append(char)

print(common_letters)