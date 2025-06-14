input = [1,2,3,4,5,6]
n = len(input)
k = 1
left = []
right = []

for i in range(k-1,-1,-1):
    left.append(input[i])
for j in range(n-1,k-1,-1):
    right.append(input[j])
output = left + right
print(output)
