class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record=[]
        for i in range(len(operations)):
            if operations[i]=='C':
                record.pop()
            elif operations[i] == '+':
                prev=record[-1]+record[-2]
                record.append(prev) 
            elif operations[i]=='D':
                record.append(2*record[-1])
            else:
                record.append(int(operations[i]))
                
        return sum(record)
