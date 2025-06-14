s = input("enter: ")

s1 = {}

for char in s:
    if char in s1:
        s1[char] += 1
    else:
        s1[char] = 1

single_appear = ""
for char, count in s1.items():
    if count == 1:
        single_appear += char
    else:
        print(f"{char}:{count}")

if single_appear:
    print(f"{single_appear}:1")
