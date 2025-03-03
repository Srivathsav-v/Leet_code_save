class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        count_dict={}
        for i in nums1:
            if i[0] in count_dict:
                count_dict[i[0]]+=i[1]
            else:
                count_dict[i[0]]=i[1]
        for i in nums2:
            if i[0] in count_dict:
                count_dict[i[0]]+=i[1]
            else:
                count_dict[i[0]]=i[1]
        ans=[]
        for key in sorted(count_dict.keys()):
            ans.append([key,count_dict[key]])
            
        return ans
    
    
        
