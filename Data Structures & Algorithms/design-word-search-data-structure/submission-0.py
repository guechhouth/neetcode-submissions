class TrieNode:
    def __init__(self):
        self.children= {}
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True
        
    def search(self, word: str) -> bool:
        #need some kind of recursion
        #dfs?

        def dfs(j, root):
            curr = root
            for i in range(j,len(word)):
                c = word[i]
                if c == ".": #backtracking
                    for child in curr.children.values():
                        #dfs, j = starting index
                        if  dfs(i+1,child):
                        #i+1 going child, skipping dot
                            return True
                    return False
                else: #normal case
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.endOfWord
        return dfs(0,self.root)
                
        
