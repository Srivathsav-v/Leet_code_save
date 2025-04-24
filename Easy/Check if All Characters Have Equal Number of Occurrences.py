class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count_dict={}
        for c in s:
            if c in count_dict:
                count_dict[c]+=1
            else:
                count_dict[c]=1

        exp=count_dict[s[0]]
        
        for k,v in count_dict.items():
            if v!=exp:
                return False
        return True
