class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastSeen = defaultdict(int)
        for i in range(len(s)):
            lastSeen[s[i]] = i
        last = lastSeen[s[0]]
        prev = -1
        res = []
        for i in range(len(s)):
            last = max(last,lastSeen[s[i]])
            if last == i:
                res.append(last-prev)
                prev = last
        return res

            

        