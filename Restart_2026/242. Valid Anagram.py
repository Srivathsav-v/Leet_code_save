class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a={}
        b={}
        if len(s)==len(t):
            for i in range(len(s)):
                if s[i] in a :
                    a[s[i]]+=1
                else:
                    a[s[i]]=1

                if t[i] in b:
                    b[t[i]]+=1
                else:
                    b[t[i]]=1
                
        else:
            return False
        
        return a==b
