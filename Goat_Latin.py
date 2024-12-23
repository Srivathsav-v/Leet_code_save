class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        ans=""
        words=sentence.split(" ")
        vowel=['a','e','i','o','u']
        count=1
        for w in words:
            if w[0].lower() in vowel:
                ans=ans+w
                ans+="ma"
                ans+="a"*count
                ans+=" "
                count+=1
                # print(ans)
            else:
                ans=ans+w[1:]
                ans=ans+w[0]
                ans+="ma"
                ans+="a"*count
                ans+=" "
                count+=1
        return ans[:len(ans)-1]
