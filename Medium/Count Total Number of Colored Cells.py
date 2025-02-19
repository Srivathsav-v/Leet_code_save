class Solution:
    def coloredCells(self, n: int) -> int:
        if n==1:
            return 1
        else:
            ans=0
            for i in range(1,n):
                ans+=i*4
        return ans+1              
