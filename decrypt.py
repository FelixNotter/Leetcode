class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = deque()
        r = len(s) - 1
        while r >= 0:
            if s[r] == "#":
                res.appendleft(chr(int(s[r-2:r])+ord("a")-1))
                r-=3
            else:
                res.appendleft(chr(int(s[r])+ord("a")-1))
                r-=1
        return "".join(res)


        # print(chr(10+ord("a")-1))
