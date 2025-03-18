class Solution:
    def countEven(self, num: int) -> int:

        def sumofdigit(x):
            s=0
            while x>0:
                n=x%10
                s+=n
                x=x//10

            return s
        count=0
        for i in range(1,num+1):
            if sumofdigit(i)%2==0:
                count+=1
        return count
