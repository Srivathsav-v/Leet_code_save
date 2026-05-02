class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        s=(n*(n+1))//2
        t=0
        for i in nums:
            t+=i
        
        return (s-t)
