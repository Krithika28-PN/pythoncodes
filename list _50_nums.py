def process_list(nums):
    mid = len(nums) // 2  # Find the middle index
    first_half = []
    second_half = []

    # Storing first half in original order
    for i in range(mid):
        first_half.append(nums[i])

    # Storing second half in decreasing order
    for i in range(len(nums) - 1, mid - 1, -1):
        second_half.append(nums[i])

    # Printing the final sequence
    result = first_half + second_half
    print(result)

# Example list of 50 numbers
numbers = list(range(1, 51))  # [1, 2, 3, ..., 50]
process_list(numbers)

