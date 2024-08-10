# Create a list of numbers from 1 to 100
numbers = list(range(1, 101))

# Convert each number to a string
number_strings = [str(number) for number in numbers]

# Join the list of strings with hyphens
hyphen_separated = '-'.join(number_strings)

# Print the result
print(hyphen_separated)
