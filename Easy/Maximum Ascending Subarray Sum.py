class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        s=nums[0]
        s1=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                s+=nums[i]
            else:
                s1=max(s1,s)
                s=nums[i]
        s1 = max(s1, s)
        return s1
            
