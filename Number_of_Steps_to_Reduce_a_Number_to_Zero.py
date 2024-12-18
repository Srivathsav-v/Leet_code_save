class Solution:
    def numberOfSteps(self, num: int) -> int:
        count=0
        n=num
        status=True
        while status == True:
            if n == 0:
                status= False
                return count
            elif n % 2 == 0 :
                n=n//2
                count+=1
            else:
                n-=1
                count+=1

