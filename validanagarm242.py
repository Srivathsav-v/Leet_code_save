class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            sdict={}
            for i in range(len(s)):
                if s[i] in sdict:
                    sdict[s[i]]+=1
                else:
                    sdict[s[i]]=1
            tdict={}
            for i in range(len(t)):
                if t[i] in tdict:
                    tdict[t[i]]+=1
                else:
                    tdict[t[i]]=1
            if sdict==tdict:
                return True
            else:
                return False
        
