class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_string = bin(n)
        print(binary_string)
        count=0
        for i in binary_string:
            if i=='1':
                count+=1
        return count
