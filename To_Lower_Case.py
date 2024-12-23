class Solution:
    def toLowerCase(self, s: str) -> str:
        ans=""
        for cal in s:
            if ord(cal)>64 and ord(cal)<91:
                # print(cal)
                res=ord("a")+(ord(cal)-ord("A"))
                ans+=chr(res)
            else:
                ans+=cal
        return ans
