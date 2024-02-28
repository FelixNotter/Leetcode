
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for letter in word:
            
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
        cur.end = True
        

    def search(self, word: str) -> bool:
        def helper(word,cur = self.root):
            for i in range(len(word)):
                if word[i] == ".":
                    found = False
                    for c in cur.children:
                        found = found or helper(word[i+1:],cur.children[c])
                    return found
                if word[i] not in cur.children :
                    return False
                cur = cur.children[word[i]]
            return cur.end
        return helper(word) 
    
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)