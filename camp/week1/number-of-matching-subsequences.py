class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self
    def insert(self,word):
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
        cur.end = True
    def search(self,word):
        cur = self.root
        i = 0
        n = len(word)
        while i < n and not cur.end:
            if word[i] in cur.children:
                i+=1
            nxt = list(cur.children.keys())
            nxt = nxt[0]

            cur = cur.children[nxt]
        if i < n:
            return False
        return True

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        newTrie = Trie()
        newTrie.insert(s)
        res = 0
        memo = {}
        for word in words:
            if word not in memo:
                memo[word] = newTrie.search(word)

            if memo[word]:
                res+=1
        return res
        