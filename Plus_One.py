class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        for num in digits:
            s+=str(num)
        
        ans=int(s)
        ans=ans+1
        s=str(ans)
        ndigit=[]
        for i in range(len(s)):
            ndigit.append(int(s[i]))

        return ndigit

        
