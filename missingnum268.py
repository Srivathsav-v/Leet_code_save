class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        totalsum=n*(n+1)//2
        numssum=0
        for i in nums:
            numssum+=i
        
        return totalsum-numssum
