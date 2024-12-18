class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        def counter(n:int,count=0) -> int:
            if n == 0:
                return count
            else:
                n=n//10
                count+=1
                return counter(n,count)
        ctr=0
        for num in nums:
            if counter(num)%2==0:
                ctr+=1
        return ctr           

