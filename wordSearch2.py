class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        
class Trie:
    def __init__(self,board):
        self.root = TrieNode()
        self.board = board
  
    def safe(self,r,c):
        ROWS = len(self.board)
        COLS = len(self.board[0])
        if 0<=r< ROWS and 0 <=c<COLS:
            return True
        return False

    def insert(self,word):

        cur = self.root
        for letter in word:

            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
  
        cur.end = True
       
    def search(self):
        ROWS = len(self.board)
        COLS = len(self.board[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        ans = set()
        def helper(r,c,root,path,w):
            cur = root
            
            if (r,c) in path:
                return 
            if self.board[r][c] not in cur.children:
                return False

            path.add((r,c))
            w+=self.board[r][c]
    
            cur = cur.children[self.board[r][c]]
        
            if cur.end:
                ans.add(w)
                cur.end = False
                
            for dr,dc in directions:
                if not self.safe(r+dr,c+dc):
                    continue
                helper(r+dr,c+dc,cur,path,w)
    
            path.remove((r,c))
  
        
        for r in range(ROWS):
            for c in range(COLS):
                helper(r,c,self.root,set(),"")
 


        return ans 
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        newTrie = Trie(board)
        for word in words:
            newTrie.insert(word)

        ROWS = len(board)
        COLS = len(board[0])

        a = newTrie.search()
        return a
        

            
                        
        

        
        

        
