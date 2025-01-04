class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ans=[]
        count=0
        for word in words:
            s=0
            e=len(word)-1
            if word[s].lower() in ('a', 'e', 'i', 'o', 'u') and word[e].lower() in ('a', 'e', 'i', 'o', 'u'):
                count+=1
                ans.append(count)
            else:
                count+=0
                ans.append(count)
        print(ans)
        final_ans=[]
        for q in queries:
            start=q[0]
            end=q[1]
            if start==0:
                final=ans[end]
                final_ans.append(final)
            # elif start==end:
            #     final=ans[end]
            #     final_ans.append(final)
            else:
                final=ans[end]-ans[start-1]
                final_ans.append(final)
        return final_ans
