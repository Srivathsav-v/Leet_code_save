class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count=0
        l=""
        count_dict={}
        for i in words:
            if i in count_dict:
                count_dict[i]+=1
            else:
                count_dict[i]=1

        for a in s:
            l+=a
            if l in words:
                if l in count_dict:
                    count+=count_dict[l]
                else:
                    count+=1

        return count
                

