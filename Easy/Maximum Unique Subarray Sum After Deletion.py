class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums1=set(nums)
        sum=0
        if max(nums)<0:
            return max(nums)
        else:
            for i in nums1:
                if i>=0:
                    sum+=i
        return sum
