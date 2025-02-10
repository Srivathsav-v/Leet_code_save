class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sm=0
        mul=1
        while n>0:
            m=n%10
            sm+=m
            mul*=m
            n=n//10

        return mul-sm
