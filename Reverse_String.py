class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s1=[]
        for i in range(len(s)-1,-1,-1):
            s1.append(s[i])
        for i in range(len(s1)):
            s[i]=s1[i]



