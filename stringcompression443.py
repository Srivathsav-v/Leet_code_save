class Solution:
    def compress(self, chars: List[str]) -> int:
        prev=chars[0]
        s=""
        count=1
        for char in chars[1:]:
            
            if char != prev:
                s+=prev
                if count > 1:
                    s += str(count)
                prev=char
                count=1
            else:
                count+=1

        # print(s)
        s+=prev
        if count > 1:
            s += str(count)
        # # print(s)
        # chars1=[]
        # for l in range(len(s)):
        #     chars1.append(s[l])

        # return len(chars1)
        chars[:] = list(s)
        
        return len(chars)


