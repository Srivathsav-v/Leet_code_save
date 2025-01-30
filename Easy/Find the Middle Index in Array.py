class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        s=0
        nums2=[]
        for n in nums:
            s+=n
            nums2.append(s)
        for i in range(len(nums)):
            if i==0:
                leftsum=0
            else:
                leftsum=nums2[i-1]
            rightsum=nums2[-1]-nums2[i]

            if leftsum==rightsum:
                return i
        return -1
