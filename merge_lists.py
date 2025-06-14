# merge two list using one for loop

# Define two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# Create an empty list to store merged elements
merged_list = []
# Iterate over both lists combined
for item in list1 + list2:
    merged_list.append(item)
# Print the merged list
print(merged_list)

# Alternate method
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
#
# # Initialize an empty list to store the merged result
# merged_list = []
#
# # Determine the length of the longer list
# max_length = max(len(list1), len(list2))
#
# # Use a single loop to merge the lists
# for i in range(max_length):
#     # Add element from list1 if it exists
#     if i < len(list1):
#         merged_list.append(list1[i])
#     # Add element from list2 if it exists
#     if i < len(list2):
#         merged_list.append(list2[i])
#
# # Print the merged list
# print(merged_list)