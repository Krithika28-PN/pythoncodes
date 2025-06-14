# set {}

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
myset = set1.union(set2)
print(myset)

myset1 = set1.intersection(set2)
print(myset1)

myset2 = set1.difference(set2)
print(myset2)
myset2 = set2.difference(set1)
print(myset2)

#subset
s1 = set1.issubset(set2)
print(s1)