class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        great=max(candies)
        ans=[]
        for c in candies:
            s=c+extraCandies
            if s < great:
                ans.append(False)
            else:
                ans.append(True)
        return ans
