class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        countdict={}
        candylimit=(len(candyType))//2
        for i in (candyType):
            if i in countdict:
                countdict[i]+=1
            else:
                countdict[i]=1
        candycount=len(countdict)
        if candylimit>candycount:
            return min(candylimit,candycount)
        else:
            return candylimit
