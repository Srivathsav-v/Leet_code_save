class Solution:
    def isValid(self, s: str) -> bool:
        matching_dict={")":"(","}":"{","]":"["}
        stack=[]
        opening=["(","{","["]
        
        for i in range(len(s)):
            
            if s[i] in opening:
                stack.append(s[i])
            elif stack and matching_dict[s[i]] == stack[-1]:
                stack.pop()
            else:
                return False
        if stack == []:
            return True
        else:
            return False
        
        
