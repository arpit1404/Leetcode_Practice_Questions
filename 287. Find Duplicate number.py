#Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and using only constant extra space.

def find_duplicate_digits(n):
    # Initialize an array to keep track of seen digits
    seen = [0] * 10  # Array of size 10 (for digits 0-9)
    
    # Loop until the number is greater than 0
    while n > 0:
        rem = n % 10  # Get the last digit
        if seen[rem] == 1:  # If the digit is already seen
            print("Yes, duplicate value found")
            return
        seen[rem] = 1  # Mark the digit as seen
        n = n // 10  # Remove the last digit from the number
    
    # If no duplicates are found
    print("No duplicate value found")

# Example usage
number = 123456789  # Replace with your number
find_duplicate_digits(number)

