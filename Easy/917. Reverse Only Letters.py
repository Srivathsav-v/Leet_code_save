class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i=0
        j=len(s)-1
        s_list = list(s)
        def is_letter(c):
            return (65 <= ord(c) <= 90) or (97 <= ord(c) <= 122)
        while i <j:
            if is_letter(s_list[i])==True and is_letter(s_list[j])==True:
                x=s_list[i]
                s_list[i]=s_list[j]
                s_list[j]=x
                i+=1
                j-=1
            elif is_letter(s_list[i])==True and is_letter(s_list[j])==False:
                j-=1
            else:
                i+=1
        return "".join(s_list)


