class Solution:
    def isHappy(self, n: int) -> bool:
        def sumofdigits(number: int, digitsum : int = 0):
            if number == 0:
                return digitsum
            else:
                digit=number%10
                digitsum+=(digit*digit)
                return sumofdigits(number//10,digitsum)
        digitsum=sumofdigits(n)
        seen=set()
        while digitsum!=1:
            if digitsum in seen:
                return False
            else:
                seen.add(digitsum)
                digitsum=sumofdigits(digitsum)
        return True
