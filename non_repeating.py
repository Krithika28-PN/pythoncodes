# # Find the first non-repeating character in a string.

s = 'testing'

# Iterate through the string and find the first non-repeated character
for i in range(len(s)):
    count = 0
    for j in range(i + 1, len(s)):    # looking for similar items in the list
        if s[i] == s[j]:
            count += 1

    if count == 0:
        print(f"The first non-repeated character is: {s[i]}")
        break
else:
    print("No non-repeated character found.")
