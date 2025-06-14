# sentence = "My name is Rohit"
# words = sentence.split()  # Split the sentence into words
# longest_word = max(words, key=len)  # Find the word with the maximum length
# print(longest_word)  # Output: "Rohit"

# OR

sentence = "My name is Rohit"
words = sentence.split()  # Split the sentence into words
#print(words)

# Initialize variables to keep track of the longest word
longest_word = ""
max_length = 0

# Loop through each word in the list
for word in words:
    if len(word) > max_length:
        longest_word = word
        max_length = len(word)

print(longest_word)  # Output: "Rohit"

