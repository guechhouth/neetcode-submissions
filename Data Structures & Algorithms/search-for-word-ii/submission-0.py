'''
use Trie to create a dictionary of of the list of word

- start backtracking dfs from varios position and check if there is prefix in dictionary 
- checking is O(1) rather than go through the whole list every time


'''
class TrieNode:
    def __init__(self):
        self.children = {} #value is child trie node
        self.isWord = False
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        row,col = len(board), len(board[0])
        res, visit = set(), set() #res= dont want to add same combination, #visit: do want to repeat same cha twice\

        def dfs(r,c,node,word): #word= word so far
            if (r<0 or c<0 or 
            r== row or c == col or 
            (r,c) in visit or 
            board[r][c] not in node.children):
                return
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            #backtracking
            visit.remove((r,c))
        for r in range(row):
            for c in range(col):
                dfs(r,c,root,"")
        return list(res)



        