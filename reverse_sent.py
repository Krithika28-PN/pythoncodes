def reverse_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    n = len(words)
    # Reverse the words using a loop
    reversed_words = []
    for i in range(n - 1, -1, -1):
        reversed_words.append(words[i])
    # Join the reversed words back into a string
    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence

print(reverse_words("Rohit is good guy"))

