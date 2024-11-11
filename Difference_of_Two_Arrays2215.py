class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        lis1=[]
        lis2=[]
        for i in set(nums1):
            if i not in nums2:
                lis1.append(i)
                
        for i in set(nums2):
            if i not in nums1:
                lis2.append(i)
            
        return [lis1,lis2]
