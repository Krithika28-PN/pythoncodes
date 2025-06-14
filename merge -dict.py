def merge_and_sum(dict1, dict2):
    # Create a new dictionary to store the result
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            # Sum values if the key exists in both dictionaries
            merged_dict[key] += value
        else:
            # Add the key-value pair if it doesn't exist in the merged dictionary
            merged_dict[key] = value
    return merged_dict

# Example dictionaries
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 15, 'c': 25, 'd': 40}

# Merge dictionaries and sum values of common keys
result = merge_and_sum(dict1, dict2)
print(result)

# dict1 = {'a': 10, 'b': 20, 'c': 30}
# dict2 = {'b': 15, 'c': 25, 'd': 40}
#
# merged_dict = dict2.copy()
#
# for key,values in dict1.items():
#     if key in merged_dict:
#         merged_dict[key] += values
#     else:
#         merged_dict[key] = values
# print(merged_dict)