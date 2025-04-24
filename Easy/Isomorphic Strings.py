class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        count_dict1={}
        count_dict2={}
        for cs , ct in zip(s,t):
            if cs in count_dict1 and count_dict1[cs]!=ct:
                return False
            if ct in count_dict2 and count_dict2[ct]!=cs:
                return False
            count_dict1[cs]=ct
            count_dict2[ct]=cs
        return True
