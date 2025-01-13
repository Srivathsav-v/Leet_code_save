class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Calculate `cdw2` using maximum frequency logic
        cdw2 = {}
        for word in words2:
            count_dict = {}
            for c in word:
                if c in count_dict:
                    count_dict[c] += 1
                else:
                    count_dict[c] = 1
            for c, count in count_dict.items():
                if c in cdw2:
                    cdw2[c] = max(cdw2[c], count)
                else:
                    cdw2[c] = count
        
        # Validate words in `words1`
        ans = []
        for word in words1:
            count_dict = Counter(word)
            isuniversal = True
            for key, val in cdw2.items():
                if key not in count_dict or count_dict[key] < val:
                    isuniversal = False
                    break
            if isuniversal:
                ans.append(word)
        return ans
