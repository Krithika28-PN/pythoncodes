# add the missing number to the list
# for this we can use summation formula


def missing_num():
    num_list = [1, 2, 3, 4, 6, 7]
    n = len(num_list) + 1  # Including the missing number

    def summation(n):
        # Correct summation formula for the first n natural numbers
        return n * (n + 1) // 2

    expected_sum = summation(n)  # Sum of first n natural numbers
    actual_sum = sum(num_list)  # Sum of numbers in the list
    missing_number = expected_sum - actual_sum  # Calculate the missing number

    return missing_number

print(missing_num())
