class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count_dict1={}
        count_dict2={}
        count=0
        for word in words1:
            if word in count_dict1:
                count_dict1[word]+=1
            else:
                count_dict1[word]=1
        for word in words2:
            if word in count_dict2:
                count_dict2[word]+=1
            else:
                count_dict2[word]=1
        for word in words1:
            if word in words2:
                if count_dict1[word]==1 and count_dict2[word]==1:
                    count+=1

        return count
