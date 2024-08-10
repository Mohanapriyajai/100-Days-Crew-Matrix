# Create a list of numbers from 111 to 2 (inclusive) in reverse order
numbers = list(range(111, 1, -1))

# Convert each number to a string
number_strings = [str(number) for number in numbers]

# Join the list of strings with hyphens
hyphen_separated = '-'.join(number_strings)

# Print the result
print(hyphen_separated)


