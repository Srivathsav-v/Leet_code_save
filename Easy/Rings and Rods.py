class Solution:
    def countPoints(self, rings: str) -> int:
        count_dict={}
        for i in range(1,len(rings),2):
            color=rings[i-1]
            rod=rings[i]
            if rod in count_dict:
                count_dict[rod].add(color)
            else:
                count_dict[rod]={color}

        count=0
        for i in count_dict:
            if count_dict[i]=={'R','G','B'}:
                count+=1
        return count
