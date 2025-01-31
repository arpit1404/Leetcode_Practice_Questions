# -------------Question 238 Leet code-------------------
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
# Constraints:
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)


#------Answer:

# We define two variables left and right to represent the product of all elements to the left and right of the current element, respectively. Initially, left=1 and right=1. We define an answer array ans of length n.
# First, we traverse the array from left to right. For the i-th element, we update ans[i] with left, then multiply left by nums[i].
# Next, we traverse the array from right to left. For the i-th element, we update ans[i] to ans[i]×right, then multiply right by nums[i].
# After the traversal, we return the answer array ans.
# The time complexity is O(n), where n is the length of the array nums. Ignoring the space consumption of the answer array, the space complexity is O(1).

# Function to calculate the product of all 
# elements except the current element
def productExceptSelf(arr):
    n = len(arr)

    # Initialize the result list as 1
    res = [1] * n

    for i in range(n):
        
        # Compute the product of all except arr[i]
        for j in range(n):
            if i != j:
                res[i] *= arr[j]

    return res

if __name__ == "__main__":
    arr = [10, 3, 5, 6, 2]
    res = productExceptSelf(arr)
    print(" ".join(map(str, res)))

