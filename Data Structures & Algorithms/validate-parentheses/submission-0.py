'''understand
char allowed: (,),{,},[,]
valid IFF:
- open has corresponding close
- open is closed in correct order
- close has corresponding open

true if valid
false if not valid
'''

class Solution:
    def isValid(self, s: str) -> bool:
        #initialize stack
        stack = []
        #initialize a dct to store the pair
        dct = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        #for each item in the s
        for c in s:
            #if the item is open 
            if c in dct.values():
                #add to the stack
                stack.append(c)

            #if it is not 
            elif c in dct:

                #check is the stack is empty and check if the top item is the corresponding 
                #open tag and pop it
                if not stack or stack[-1] != dct[c]:
                    return False
                stack.pop()
            else:
                return False
        #if the stack is empty
        #return true 
        if not stack:
            return True
        return False
        