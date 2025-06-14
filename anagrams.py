s1 = "listen"
s2 = "silent"

if len(s1) == len(s2):  # Check if lengths are equal
    freq_s1 = {}
    freq_s2 = {}

    # Count characters in s1
    for char in s1:
        if char in freq_s1:
            freq_s1[char] += 1  # Increment count if key exists
        else:
            freq_s1[char] = 1  # Initialize with 1

    # Count characters in s2
    for char in s2:
        if char in freq_s2:
            freq_s2[char] += 1  # Increment count if key exists
        else:
            freq_s2[char] = 1  # Initialize with 1

    print(freq_s1, freq_s2)

    # Compare the two frequency dictionaries
    if freq_s1 == freq_s2:
        print("Anagram")
    else:
        print("Not Anagram")
else:  # Lengths are not equal
    print("Not Anagram")
