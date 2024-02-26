class Solution:
    def maxProduct(self, words: List[str]) -> int:
        precompute = [0]*len(words)
        for i in range(len(words)):
            precompute[i] = self.bits(words[i])
        
        res = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if not (precompute[i] & precompute[j]):
                    res = max(res,len(words[i])*len(words[j]))
        return res


    def bits(self,word):
        ans = 0
        for letter in word:
            ans|=(1<<(ord(letter)-ord("a")))
        return ans
            