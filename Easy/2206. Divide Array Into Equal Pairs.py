class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        count_dict={}
        for i in nums:
            if i in count_dict:
                count_dict[i]+=1
            else:
                count_dict[i]=1
        print(count_dict)
        for i in count_dict:
            if count_dict[i]%2==1:
                
                return False
        return True
