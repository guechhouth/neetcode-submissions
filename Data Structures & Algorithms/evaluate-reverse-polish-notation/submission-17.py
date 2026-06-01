"""
tokens = ["1","2","+","3","*","4","-"]
- the first two positions are always two
- then operation then digit then operation again

let's pop everything: [-,4,*,3,+,2,1]
"""
import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ## operation map
        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

        if len(tokens) == 1 and tokens[-1].isnumeric():
            return int(tokens[-1])
        if len(tokens) == 0:
            return 0
        
        # processing the digits
        total = 0
        cal = []
        for i in tokens:
            if i not in operations:
                cal.append(int(i))
            elif i in operations:
                #pop all value from cal
                print(f"cal: {cal}")
                a = cal.pop()
                b = cal.pop()
                # if one of them is negative we need to do ceiling
                print(f"cal: {cal}")
                if i == "/":
                    total = int(b/a)
                else:
                    total = operations[i](b, a)
                cal.append(total)
                print(f"cal: {cal}\n")

        # top of the cal stack
        return cal[-1]
            




        