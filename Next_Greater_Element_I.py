class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index_dict={}
        ans=[]
        for i in range(len(nums2)):
            index_dict[nums2[i]]=i

        for i in nums1:
            index=index_dict[i]
            status=False
            for j in range(index+1,len(nums2)):
                if nums2[j] > i:
                    ans.append(nums2[j])
                    status=True
                    break
            if status==False:
                ans.append(-1)
            
        return ans
