class Solution:

    def encode(self, strs: List[str]) -> str:
        '''
        #encode a list of string into a single string
        #design question: we need to decide how to present the output 
        string such that it will be conveient to convert it back to list
        #1: joining them together --> hard to decode back
        #2: putting a number or symbol b/w each word --> what if there is the same number/symbol in that word
        #3: list --> how are we storig list
        #4: number which is the length infront of each word + another symbol
        '''
        
        string = ""
        for s in strs:
            string += str(len(s)) + ":" + s
        return string

    def decode(self, s: str) -> List[str]:
        lst = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != ":":
                j = j + 1
        
            length = int(s[i:j])
            lst.append(s[j+1:j+1+length])

            i = j + 1 + length
        return lst
        
