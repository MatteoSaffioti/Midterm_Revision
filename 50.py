import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Print the original list
print("Original List:", random_numbers)

# Replace numbers greater than 50 with "XX"
random_numbers = ["XX" if num > 50 else num for num in random_numbers]

# Print the modified list
print("Modified List:", random_numbers)

