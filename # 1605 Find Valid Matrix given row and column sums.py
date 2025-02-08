# 1605. Find Valid Matrix Given Row and Column Sums
# Medium
# Topics
# Companies
# Hint
# You are given two arrays rowSum and colSum of non-negative integers where rowSum[i] is the sum of the elements in the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

# Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum requirements.

# Return a 2D array representing any matrix that fulfills the requirements. It's guaranteed that at least one matrix that fulfills the requirements exists.

 

# Example 1:

# Input: rowSum = [3,8], colSum = [4,7]
# Output: [[3,0],
#          [1,7]]
# Explanation: 
# 0th row: 3 + 0 = 3 == rowSum[0]
# 1st row: 1 + 7 = 8 == rowSum[1]
# 0th column: 3 + 1 = 4 == colSum[0]
# 1st column: 0 + 7 = 7 == colSum[1]
# The row and column sums match, and all matrix elements are non-negative.
# Another possible matrix is: [[1,2],
#                              [3,5]]
# Example 2:

# Input: rowSum = [5,7,10], colSum = [8,6,8]
# Output: [[0,5,0],
#          [6,1,0],
#          [2,0,8]]
 

# Constraints:

# 1 <= rowSum.length, colSum.length <= 500
# 0 <= rowSum[i], colSum[i] <= 108
# sum(rowSum) == sum(colSum) write a program in python optimized code and help me understand the code consider you are explaining this code to beginner python programmer 


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # Initialize the result matrix with zeros
        rows, cols = len(rowSum), len(colSum)
        matrix = [[0] * cols for _ in range(rows)]
        
        # Iterate over each row and column
        for i in range(rows):
            for j in range(cols):
                # Take the minimum of remaining row sum and column sum
                matrix[i][j] = min(rowSum[i], colSum[j])
                
                # Subtract the value placed in matrix from rowSum and colSum
                rowSum[i] -= matrix[i][j]
                colSum[j] -= matrix[i][j]
        
        return matrix


# Code Overview:
# This function constructs a 2D matrix where:

# The sum of elements in each row matches the rowSum array.
# The sum of elements in each column matches the colSum array. The function uses a greedy approach to fill in the matrix, ensuring that at every step, the row and column sum constraints are maintained.
# Sample Input:
# Let's use this example:

# python
# Copy
# Edit
# rowSum = [3, 8]
# colSum = [4, 7]
# Step-by-Step Explanation:
# python
# Copy
# Edit
# class Solution:
#     def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
# We define a class Solution and a method restoreMatrix.
# The method takes two inputs:
# rowSum: A list representing the sum of elements in each row.
# colSum: A list representing the sum of elements in each column.
# Step 1: Initialize the Result Matrix
# python
# Copy
# Edit
# rows, cols = len(rowSum), len(colSum)
# matrix = [[0] * cols for _ in range(rows)]
# rows and cols store the number of rows and columns in the matrix, derived from the length of rowSum and colSum, respectively.

# For the given input:

# python
# Copy
# Edit
# rows = 2  # Because rowSum has 2 elements
# cols = 2  # Because colSum has 2 elements
# matrix is initialized as a 2D list of zeros, with dimensions [rows x cols]. This matrix will store the values that we need to calculate.

# After initialization:

# python
# Copy
# Edit
# matrix = [[0, 0], [0, 0]]
# Step 2: Iterate Through the Matrix
# python
# Copy
# Edit
# for i in range(rows):
#     for j in range(cols):
# We use two nested loops:
# The outer loop (for i in range(rows)) iterates through each row.
# The inner loop (for j in range(cols)) iterates through each column.
# Step 3: Fill the Matrix Based on Row and Column Sums
# python
# Copy
# Edit
# matrix[i][j] = min(rowSum[i], colSum[j])
# At each position matrix[i][j], we fill the value as the minimum of:
# rowSum[i]: The remaining sum for row i.
# colSum[j]: The remaining sum for column j.
# The reason we take the min value is that we want to ensure that the element we place does not exceed the remaining row sum or column sum.

# First Iteration (i=0, j=0):
# rowSum[0] = 3 and colSum[0] = 4
# matrix[0][0] = min(3, 4) = 3
# After updating the matrix:

# python
# Copy
# Edit
# matrix = [[3, 0], [0, 0]]
# Step 4: Update the Row and Column Sums
# python
# Copy
# Edit
# rowSum[i] -= matrix[i][j]
# colSum[j] -= matrix[i][j]
# After placing a value in matrix[i][j], we update the rowSum and colSum arrays by subtracting the value we just placed.
# For matrix[0][0] = 3:

# rowSum[0] = 3 - 3 = 0
# colSum[0] = 4 - 3 = 1
# After updating the sums:

# python
# Copy
# Edit
# rowSum = [0, 8]
# colSum = [1, 7]
# Second Iteration (i=0, j=1):
# rowSum[0] = 0 and colSum[1] = 7
# matrix[0][1] = min(0, 7) = 0
# After updating the matrix:

# python
# Copy
# Edit
# matrix = [[3, 0], [0, 0]]
# Update the sums:

# rowSum[0] = 0 - 0 = 0
# colSum[1] = 7 - 0 = 7
# After updating the sums:

# python
# Copy
# Edit
# rowSum = [0, 8]
# colSum = [1, 7]
# Third Iteration (i=1, j=0):
# rowSum[1] = 8 and colSum[0] = 1
# matrix[1][0] = min(8, 1) = 1
# After updating the matrix:

# python
# Copy
# Edit
# matrix = [[3, 0], [1, 0]]
# Update the sums:

# rowSum[1] = 8 - 1 = 7
# colSum[0] = 1 - 1 = 0
# After updating the sums:

# python
# Copy
# Edit
# rowSum = [0, 7]
# colSum = [0, 7]
# Fourth Iteration (i=1, j=1):
# rowSum[1] = 7 and colSum[1] = 7
# matrix[1][1] = min(7, 7) = 7
# After updating the matrix:

# python
# Copy
# Edit
# matrix = [[3, 0], [1, 7]]
# Update the sums:

# rowSum[1] = 7 - 7 = 0
# colSum[1] = 7 - 7 = 0
# After updating the sums:

# python
# Copy
# Edit
# rowSum = [0, 0]
# colSum = [0, 0]
# Step 5: Return the Final Matrix
# python
# Copy
# Edit
# return matrix
# The matrix is now filled correctly:
# python
# Copy
# Edit
# matrix = [[3, 0], [1, 7]]
# Final Output:
# The function returns:

# python
# Copy
# Edit
# [[3, 0],
#  [1, 7]]
# This matrix satisfies both row sums and column sums:

# Row sums: 3 + 0 = 3 and 1 + 7 = 8
# Column sums: 3 + 1 = 4 and 0 + 7 = 7
# Summary:
# Greedy filling: For each matrix cell, we take the minimum of the remaining row sum and column sum.
# Updating sums: After filling each cell, we subtract the placed value from both the row sum and column sum.
# Repeat: We continue this process until the matrix is completely filled.
# This ensures that the resulting matrix will always satisfy the row and column sum constraints.