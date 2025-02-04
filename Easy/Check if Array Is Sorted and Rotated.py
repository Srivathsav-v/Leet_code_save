class Solution:
    def check(self, nums: List[int]) -> bool:
        
        # for i in range(0,len(nums)-1):
        #     if nums[i+1]==nums[i]+1:
        #         continue
        #     else:
        #         prev=nums[i]-nums[i+1]
        #         print(prev)
        #         print(nums[i-1])
        #         print(nums[i])
        #         print(nums[i+1])
        #         if nums[i-1]!=prev:
        #             return False
        # return True
        count=0
        for i in range(0,len(nums)-1):
            if nums[i]>nums[i+1]:
                count+=1
        if nums[-1] > nums[0]:
            count += 1      
        if count <= 1:
            return True
        return False
