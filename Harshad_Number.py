class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:

        def sumofdigits(x:int,sum=0):
            if x==0:
                return sum
            else:
                sum+=x%10
                x=x//10
                return sumofdigits(x,sum)
        
        s=sumofdigits(x)
        if x % s == 0:
            return s
        return -1
