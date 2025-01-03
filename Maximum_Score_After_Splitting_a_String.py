class Solution:
    def maxScore(self, s: str) -> int:
        ans=0
        for i in range(1,len(s)):
            a=s[:i]
            
            b=s[i:]
            c1=0
            c2=0
            for i in a:
                if i=="0":
                    c1+=1
            for j in b:
                if j=="1":
                    c2+=1
            ans=max(ans,c1+c2)
        return ans
