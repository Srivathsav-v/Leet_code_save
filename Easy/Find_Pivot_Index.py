from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = 0
        nums2 = []
        
        for n in nums:
            s += n
            nums2.append(s)
        
        for i in range(len(nums)):
            if i == 0:
                left_sum = 0 
            else:
                left_sum = nums2[i - 1]
        
            right_sum = nums2[-1] - nums2[i] 
            
            if left_sum == right_sum:
                return i
        
        return -1  
