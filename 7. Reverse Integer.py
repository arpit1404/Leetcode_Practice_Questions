# Input number
number = 2345

# Convert the number to a string to easily access individual digits
digits = list(str(number))

# Reverse the list of digits
reversed_digits = digits[::-1]

# Join the reversed digits back into a string and convert to an integer
reversed_number = int("".join(reversed_digits))

# Print the reversed number
print("Reversed number:", reversed_number)