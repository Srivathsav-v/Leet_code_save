class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_string = bin(n)
        print(binary_string)
        count=0
        for bs in binary_string:
            if bs == "1":
                count+=1
        return count
