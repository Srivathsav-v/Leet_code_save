class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        countdict={}
        for i in range(len(s)):
            countdict[indices[i]]=s[i]

        ans=""
        for i in range(len(s)):
            ans+=(countdict[i])
        return ans
