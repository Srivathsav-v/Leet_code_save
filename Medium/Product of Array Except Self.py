class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        postfix=[]
        m=1
        for i in nums:
            m=m*i
            prefix.append(m)
        m=1
        for i in range(len(nums)-1,-1,-1):
            m=nums[i]*m
            postfix.append(m)
        postfix.reverse()
        print(prefix)
        print(postfix)
        for i in range(len(nums)):
            if i==0:
                nums[i]=1*postfix[i+1]
            elif i==len(nums)-1:
                nums[i]=prefix[i-1]*1
            else:
                nums[i]=prefix[i-1]*postfix[i+1]

        return nums
