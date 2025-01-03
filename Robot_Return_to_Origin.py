class Solution:
    def judgeCircle(self, moves: str) -> bool:
        count_dict={'U':0,'D':0,'L':0,'R':0}
        for move in moves:
            if move in count_dict:
                count_dict[move]+=1
        
        s=sum(count_dict.values())
        if count_dict['U']==count_dict['D'] and count_dict['R']==count_dict['L']:
            return True
        return False
