class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        count_dict={}
        for i in nums:
            if i in count_dict:
                count_dict[i]+=1
            else:
                count_dict[i]=1
        # print(count_dict)   
        for k,v in count_dict.items():
            if v==1:
                return k
        
