class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count_dict={}
        for word in s1.split(" "):
            if word in count_dict:
                count_dict[word]+=1
            else:
                count_dict[word]=1
        for word in s2.split(" "):
            if word in count_dict:
                count_dict[word]+=1
            else:
                count_dict[word]=1
        lis=[]
        for w,c in count_dict.items():
            if c==1:
                lis.append(w)

        return lis 
