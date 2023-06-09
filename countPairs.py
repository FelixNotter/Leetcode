class Solution:
    def similarPairs(self, words: List[str]) -> int:
        res = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if set(words[j]) == set(words[i]):
                    res += 1
        return res
