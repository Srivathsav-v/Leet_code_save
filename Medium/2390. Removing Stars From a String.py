class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for l in s:
            if l=="*":
                if stack:
                    stack.pop()
            else:
                stack.append(l)
        a=""
        for i in stack:
            a+=i
        return a
