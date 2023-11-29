class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        res = []
        
        count = Counter(words)
        heap = [(-count[word],word)for word in count]
        heapify(heap)
        while k>0:
            num,word = heappop(heap)
            res.append(word)
            k-=1
        return res
        

        