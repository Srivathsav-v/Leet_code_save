class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        s=str(num)
        a=""
        for i in range(len(s)-1,-1,-1):
            a+=s[i]
        rev=(int(a))
        s=str(rev)
        a=""
        for i in range(len(s)-1,-1,-1):
            a+=s[i]
        rerev=int(a)
        if rerev==num:
            return True
        return False
