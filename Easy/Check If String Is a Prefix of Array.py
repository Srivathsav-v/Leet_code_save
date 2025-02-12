class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        a=""
        for w in words:
            a+=w
            if a==s:
                return True
        return False
        
