class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum=0
        ans=0
        for l in accounts:
            for i in range(len(l)):
                sum+=l[i]
            ans=max(ans,sum)
            sum=0
        return ans
