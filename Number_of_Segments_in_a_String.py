class Solution:
    def countSegments(self, s: str) -> int:
        ans=[]
        if s=="" or s.isspace():
            return 0
        else:
            for i in s.split(" "):
                if i!="":
                    ans.append(i)
        return len(ans)
