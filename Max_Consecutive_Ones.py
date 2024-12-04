class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter=0
        ch=0
        for num in nums:
            if num == 1:
                counter+=1
            else:
                ch=max(ch,counter)
                counter=0
        if nums[-1]==1:
            ch=max(ch,counter)
        return ch
    
