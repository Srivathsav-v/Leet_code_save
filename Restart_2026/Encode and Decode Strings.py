class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res+=str(len(s))+"#"+s
        print (res)
        return res

    def decode(self, s: str) -> List[str]:
        i=0
        j=0
        ans=[]
        while i < len(s):
            if s[j] !="#":
                j+=1
            else:
                print(s[i:j])
                l=int(s[i:j])
                start=j+1
                end=start+l
                print(s[start:end])
                ans.append(s[start:end])
                i=end
                j=i+1
        print(ans)
        return ans
        

            


