class Solution:
    def scoreOfString(self, s: str) -> int:
        a=[]
        for s in s:
            a.append(ord(s))
        tot=0
        for i in range(len(a)-1):
            tot+=abs(a[i]-a[i+1])

        return tot
            
