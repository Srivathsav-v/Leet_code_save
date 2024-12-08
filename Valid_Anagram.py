class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countdict1={}
        countdict2={}
        for ch in s:
            if ch in countdict1:
                countdict1[ch]+=1
            else:
                countdict1[ch]=1

        for ch in t:
            if ch in countdict2:
                countdict2[ch]+=1
            else:
                countdict2[ch]=1

        if countdict1==countdict2:
            return True
        else:
            return False      
