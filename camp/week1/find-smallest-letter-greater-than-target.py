class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        key = target
        l = 0
        r = len(letters)-1
        while l < r:
            m = l+(r-l)//2
            if letters[m] > key:
                r = m
            else:
                l = m+1
        if letters[l] > key:
            return letters[l]
        return letters[0]
        