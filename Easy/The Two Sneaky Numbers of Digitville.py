class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        s={}
        ans=[]
        for n in nums:
            if n in s:
                ans.append(n)
            else:
                s[n]=1
        return ans


