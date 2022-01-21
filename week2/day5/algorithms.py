Class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

nums = [-2,1,-3,4,-1,2,1,-5,4]

for number in nums:
    currentLargestSum = nums[0]
