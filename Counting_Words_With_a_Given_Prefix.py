class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count=0
        for word in words:
            if len(word)>=len(pref):
                wordpref=word[:len(pref)]
                if wordpref==pref:
                    count+=1
        return count
