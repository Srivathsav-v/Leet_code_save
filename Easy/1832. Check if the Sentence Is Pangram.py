class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        count_dict={}
        for i in range(ord('a'), ord('z') + 1):
            count_dict[chr(i)]=0
        for s in sentence:
            if s in count_dict:
                count_dict[s]+=1
        for l,count in count_dict.items():
            if count<1:
                return False
        return True
