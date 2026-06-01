'''
clarifying question: 
- are words and prefixes are in lowercase english letters?
- how do we treat duplicate word? do we just ignore it if it is alr in the tree during insertion?
- is there a time and space complexity i need to fulfill? 

Trie:
- Tree
- root node = start node
- each node after ->store one char
- dictionary to store the node. every time insert new character/node, we are gonna add it as a child of our
pevious node
- boolean field that indicate if the end of the word is reached : search
 
 for searching: if not mark as a word --> return false
 - if we have word 'apple', search for 'apple' -> return True
 - search for 'app' --> return False

 for startsWith:
- if we have apple, we search startsWith "app" --> return True

if there is no startsWith: we could just use Hashmap or set to add word and search for word O(1) time

analysing time complexity: only depends on the length of the word not size of trie
- checking prefix: worst case O(26) --> O(1)

'''
#initialize TrieNode
class TrieNode:
    def __init__(self):
         #create trie node
        self.children = {} #childnode 26 possible children of a node
        self.endOfWord = False

        #E.g: children["a"] = TrieNode()

class PrefixTree:

    def __init__(self):
        self.root = TrieNode() #initialize a root
       
    def insert(self, word: str) -> None:
        #iterate through every single character in the word
        curr = self.root
        for c in word:
            if c not in curr.children:
                #create a node
                curr.children[c] = TrieNode()
            #if char alr exist, set curr to that child and move to that character
            curr = curr.children[c]
        #done mark end of word
        curr.endOfWord = True
    def search(self, word: str) -> bool:
        #start at root
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        #if endOfword is set to true
        return curr.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        #start at root
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        #not checking if it is a word, just need to return True
        return True
        
        