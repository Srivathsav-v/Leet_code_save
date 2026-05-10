class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        topcount=0
        for n in numset:

            if n-1 not in numset:
                count=1
                j=True
                nnum=n+1
                while j==True:
                    if nnum in numset:
                        count+=1
                        nnum+=1
                    else:
                        topcount=max(count,topcount)
                        j=False
        return topcount
