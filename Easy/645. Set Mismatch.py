class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count_dict={}
        for i in range(1,len(nums)+1):
            count_dict[i]=0
        

        for i in nums:
            if i in count_dict:
                count_dict[i]+=1
        duplicate, missing = 0, 0
        for k,v in count_dict.items():
            if v==2:
                duplicate=k
            elif v==0:
                missing=k
        return [duplicate,missing]
            
        return ans
