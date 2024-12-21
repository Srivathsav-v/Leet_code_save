    def lengthOfLastWord(self, s: str) -> int:
        countdict={}
        for word in (s.split(" ")):
            countdict[word]=len(word)
        last_key=countdict[-1]
        last_word=countdict[last_key]
        return len(last_word)
