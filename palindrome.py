s = "kayak"

s2 = ''

for i in s:
    s2 = i + s2
print(s2)
if s == s2:
    print("palindrome")
else:
    print("Not palindrome")