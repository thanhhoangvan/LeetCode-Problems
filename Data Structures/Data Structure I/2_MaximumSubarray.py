class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        max = nums[0]
        for i in range(1,len(nums)):
            current += nums[i]
            if current < nums[i]:
                current = nums[i] 
            if max < current:
                max = current
        return max