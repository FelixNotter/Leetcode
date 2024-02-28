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
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
        cur.end = True
    def search(self,word):
        cur = self.root
        i = -1
        for letter in word:
            if letter not in cur.children:
                return i
            cur = cur.children[letter]
            i+=1
        return i
    



class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        newTrie = Trie()
        newTrie.insert(strs[0])
        j = len(strs[0])-1
        for i in range(1,len(strs)):
            j = min(j,newTrie.search(strs[i]))
        return strs[0][:j+1]