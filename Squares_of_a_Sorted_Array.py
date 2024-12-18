class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left=0
        right=len(nums)-1
        ans=[]
        while left<=right:
            if nums[left]*nums[left]<nums[right]*nums[right]:
                ans.append(nums[right]*nums[right])
                right-=1
            else:
                ans.append(nums[left]*nums[left])
                left+=1
        return ans[::-1]
