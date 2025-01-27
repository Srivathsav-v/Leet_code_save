class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def povof3(n):
            if n == 0:  
                return True
            if n % 3==2: 
                return False
            
            return povof3(n // 3)
        
        return povof3(n)

