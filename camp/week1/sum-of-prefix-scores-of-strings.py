class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.count = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            
            cur = cur.children[letter]
            cur.count+=1
            
        cur.end = True
    def search(self,word):
        cur = self.root
        res = 0
        for letter in word:
            cur = cur.children[letter]
            res+=cur.count
        return res
          
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        newTrie = Trie()
        for word in words:
            newTrie.insert(word)
        ans = []
        for word in words:
            ans.append(newTrie.search(word))
        return ans
        