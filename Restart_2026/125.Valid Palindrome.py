class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        b=""
        for i in s:
            if i.isalnum():
                a+=i
                b=i+b

        if a.lower()==b.lower():
            return True
        else:
            return False
