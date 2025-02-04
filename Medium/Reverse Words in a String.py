class Solution:
    def reverseWords(self, s: str) -> str:
        sl=[]
        for i in s.split(" "):
            if i !="":
                sl.append(i)
        ans=""
        for i in range(len(sl)-1,-1,-1):
            ans+=sl[i]
            if i!=0:
                ans+=" "
        return ans

        
