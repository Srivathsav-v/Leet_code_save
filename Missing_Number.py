class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        total_sum=n*(n+1)//2
        for i in range(len(nums)):
            ans+=nums[i]
        return total_sum-ans
