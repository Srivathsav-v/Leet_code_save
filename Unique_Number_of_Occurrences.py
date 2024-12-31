class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_dict={}

        for val in arr:
            if val in count_dict:
                count_dict[val]+=1
            else:
                count_dict[val]=1
        values=count_dict.values()
        if len(values) != len(set(values)):
            return False
        return True
