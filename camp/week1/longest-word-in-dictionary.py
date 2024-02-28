class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        cur = self.root
        num = 0
        for letter in word:
            if letter not in cur.children:
                if num == 1:
                    return False
                cur.children[letter] = TrieNode()
                
                num+=1
            cur = cur.children[letter]
        return True
        


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        print(words)

        newTrie = Trie()
        res = ""
        skip = set(words)
        for i in range(len(words)):
            ans = newTrie.insert(words[i])
            if not ans or words[i][0] not in skip:
                continue
            
            if ans and len(words[i]) > len(res):
               
                res = words[i]
        print(skip)
        return res

        