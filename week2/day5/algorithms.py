# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.
# 9:12
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:

nums = [-2,1,-3,4,-1,2,1,-5,4]

for number in nums:
    # currentLargestSum = nums[0] + nums[1]
    for num in nums:
       sum = number + num
       print(sum,end=" ")
    print()

    
