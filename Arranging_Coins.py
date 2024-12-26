class Solution:
    def arrangeCoins(self, n: int) -> int:
        count=0
        level=1
        while(n>0):
            level+=1
            n=n-level
            count+=1
            if n<=0:
                return count

        return count
