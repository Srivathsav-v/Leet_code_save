class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n=columnNumber
        ans=''
        while n > 0:
            n-=1
            rem=n%26
            ans=chr(rem+65)+ans
            n=n//26
        return ans



