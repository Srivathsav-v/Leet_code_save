class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        count_dict={}
        for i in items1:
            if i[0] in count_dict:
                count_dict[i[0]]+=i[1]
            else:
                count_dict[i[0]]=i[1]
        for i in items2:
            if i[0] in count_dict:
                count_dict[i[0]]+=i[1]
            else:
                count_dict[i[0]]=i[1]
        ans=[]
        for k,v in count_dict.items():
            ans.append([k,v])
        ans.sort()
        return ans

        
