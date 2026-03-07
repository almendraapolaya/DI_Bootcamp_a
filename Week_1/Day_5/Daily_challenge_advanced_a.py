# ==============================
# Daily challenge : Advanced Algorithm
# ==============================

# Instructions
# Here is a python code that generates a list of 20000 random numbers, called list_of_numbers, and a target number.
# import random
# list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
# target_number   = 3728

# For example
# 1000 and 2728 sums to the target_number 3728
# 1864 and 1864 sums to the target_number 3728

import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728


def find_sum_pairs(numbers, target):
    seen = set()
    found_pairs = set()

    for num in numbers:
        complement = target - num
        if complement in seen:
            pair = tuple(sorted((num, complement)))
            found_pairs.add(pair)
        seen.add(num)
    return found_pairs

results = find_sum_pairs(list_of_numbers, target_number)

print(f"Target Number: {target_number}")
print(f"Found {len(results)} unique pairs:")
print("-" * 30)

for p in results:
    print(f"{p[0]} + {p[1]} = {target_number}")