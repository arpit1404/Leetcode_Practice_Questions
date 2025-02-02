def reverse_number(number):
    # Step 1: Handle negative numbers
    is_negative = number < 0
    number = abs(number)  # Work with the absolute value

    # Step 2: Initialize the reversed number
    reversed_number = 0

    # Step 3: Reverse the number using a loop
    while number > 0:
        digit = number % 10  # Extract the last digit
        reversed_number = reversed_number * 10 + digit  # Append the digit to the reversed number
        number = number // 10  # Remove the last digit from the original number

    # Step 4: Handle negative numbers (again)
    return -reversed_number if is_negative else reversed_number

# Input number
number = -2345

# Reverse the number
reversed_number = reverse_number(number)

# Print the reversed number
print("Reversed number:", reversed_number)
