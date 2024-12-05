class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def recurs(n:int):
            if n==1:
                return True
            elif n<=0:
                return False
            else:
                if n %2==0 :
                    return recurs(n//2)
                else:
                    return False
        return recurs(n)
            

            
