class Solution:
    def makeFancyString(self, s: str) -> str:
        
        if len(s)>2:
            prev=s[1]
            prevprev=s[0]
            
            ans=s[0]+s[1]
            for i in range(2,len(s)):
                if s[i] == prev and s[i]==prevprev:
                    continue

                ans+=s[i]
                prevprev=prev
                prev=s[i]


            return ans
        else:
            return s
        





# strdict={}
        # ans=""
        # for i in range(len(s)):
        #     if s[i] in strdict:
        #         strdict[s[i]]+=1
        #     else:
        #         strdict[s[i]]=1

        # # print(strdict)
        # for i in strdict:
        #     if strdict[i] >= 3:
        #         strdict[i]=2
        # # print(strdict)

        # for i in strdict:
        #     ans+=i*strdict[i]

        # return ans
