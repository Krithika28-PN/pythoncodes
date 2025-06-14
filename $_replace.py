s = ['aishwarya', 'rohit', 'ishwari']
s2 = []

for word in s:
    first_letter = word[0]
    transformed_word = first_letter  # Start with the first letter unchanged and to keep first_letter unchanged
    for char in word[1:]:  # Iterate over the rest of the word
        if char == first_letter:
            transformed_word = transformed_word + '$'  # Replace repeated first letters with $
        else:
            transformed_word = transformed_word + char  # Keep other characters unchanged
    s2.append(transformed_word)  # Add the transformed word to the list

print(" ".join(s2))






