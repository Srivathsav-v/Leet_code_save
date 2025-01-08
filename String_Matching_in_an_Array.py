class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        count_dict={}
        lis=[]
        for i in words:
            for j in words:
                if i!=j :
                    if i in j:
                        if i not in lis:
                            lis.append(i)
        return lis
