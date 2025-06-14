s = 'Rohit banik'
vowels = 'AEIOUaeiou'
vowels_count = 0
consonants_count = 0

for char in s:
    if char in vowels:
        vowels_count += 1
    elif char not in vowels and char != ' ':
        consonants_count += 1

print(f"Count of Vowels = {vowels_count}")
print(f"Count of Consonants = {consonants_count}")


