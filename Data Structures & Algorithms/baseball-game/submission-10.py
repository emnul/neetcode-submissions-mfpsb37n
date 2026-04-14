class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        score = 0
        for op in operations:
            try:
                num = int(op)
                record.append(num)
            except ValueError:
                if op == "+":
                    tmp2 = record.pop()
                    tmp1 = record.pop()
                    tmp3 = tmp1 + tmp2
                    record.append(tmp1)
                    record.append(tmp2)
                    record.append(tmp3)
                elif op == "D":
                    tmp1 = record.pop()
                    tmp2 = tmp1 * 2
                    record.append(tmp1)
                    record.append(tmp2)
                elif op == "C":
                    record.pop()
        
        for num in record:
            score += num
        
        return score
