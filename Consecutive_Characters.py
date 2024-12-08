class Solution:
    def maxPower(self, s: str) -> int:
        ans=1
        count=1
        prev=s[0]
        for ch in range(1,len(s)):
            if s[ch] == prev:
                count+=1
                prev=s[ch]
                ans=max(ans,count)
            else:
                count=1
                prev=s[ch]
        return ans
