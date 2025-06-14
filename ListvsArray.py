# Using List
my_list = [1, 2, 3, "hello"]  # Mixed types allowed

# Using Array (from array module)
import array
my_array = array.array('i', [1, 2, 3, 4])  # Only integers allowed ('i' denotes integer type)

import numpy as np
np_array = np.array([1, 2, 3, 4])  # More optimized for numerical operations

import numpy as np
string_array = np.array(["apple", "banana", "cherry"], dtype=str)
print(string_array[1])  # Output: banana

