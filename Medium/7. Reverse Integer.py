class Solution:
    def reverse(self, x: int) -> int:
        s=str(abs(x))
        a=""
        for i in range(len(s)-1,-1,-1):
            a+=s[i]
        rev=(int(a))
        # if x>0:
        #     return rev
        # return 0-rev

        m=-2147483648
        n=2147483647
        if m<rev<n:
            if x>0:
                return rev
            return 0-rev
        return 0
