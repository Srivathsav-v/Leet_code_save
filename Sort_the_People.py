class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        count_dict={}
        for i in range(len(names)):
            count_dict[heights[i]]=names[i]
        l=[]
        for val,name in count_dict.items():
            l.append(val)
        l.sort(reverse=True)
        ans=[]
        for i in l:
            ans.append(count_dict[i])
        return ans
