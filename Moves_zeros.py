class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        left=0
        right=len(nums)-1
        while left <= right:
            if nums[left]==0 and nums[right] !=0:
                x=nums[left]
                nums[left]=nums[right]
                nums[right]=x
            elif nums[left]!=0:
                left+=1
            elif nums[right]==0:
                right-=1

                so this is doing the job but it is not maintaining the order....

                Output :-[12,1,3,0,0] Expected op :-[1,3,12,0,0]
        """
        left=0
        for i in range(len(nums)):
            if nums[i]!=0:
                x=nums[i]
                nums[i]=nums[left]
                nums[left]=x
                left+=1
                

