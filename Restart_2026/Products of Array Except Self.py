class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        noofzeros=0
        product=1
        ans=[]
        for n in nums:
            if n==0:
                noofzeros+=1
            else:
                product*=n
        
        if noofzeros>1:
            return [0]*len(nums)
        elif noofzeros==1:
            for i in nums:
                if i==0:
                    ans.append(product)
                else:
                    ans.append(0)
        else:
            for i in nums:
                ans.append(product//i)
        return ans

