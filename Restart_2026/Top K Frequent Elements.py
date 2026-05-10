class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter={}
        for n in nums:
            if n in counter:
                counter[n]+=1
            else:
                counter[n]=1
        s=sorted(counter.items(),key=lambda pair:pair[1],reverse=True)
        print(s)
        ans=[]
        for pair in s:
            ans.append(pair[0])
            if len(ans)==k:
                break
        return ans
            
