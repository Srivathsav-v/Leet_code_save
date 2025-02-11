class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for ch in s:
            if ch.isnumeric():
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        ans=""
        for s in stack:
            ans+=s
        return ans
