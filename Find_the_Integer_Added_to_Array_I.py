class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        s1=sum(nums1)
        s2=sum(nums2)
        if s1>s2:
            rem=s1-s2
            return -rem//len(nums1)
        rem=s2-s1
        return rem//len(nums1)
