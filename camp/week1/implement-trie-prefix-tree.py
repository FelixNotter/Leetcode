
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        cur = self.root
        for letter in word:
            
            if letter not in cur.children :
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
        cur.end = True
    def search(self,word):
        cur = self.root
        for letter in word:
            
            if letter not in cur.children:
                return False
            cur = cur.children[letter]
        return cur.end 
    def startsWith(self,word):
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                return False
            cur = cur.children[letter]
        return True 




# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)