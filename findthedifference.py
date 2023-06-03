class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        check = Counter(s)
        for letter in t:
            if not check[letter]:
                return letter
            check[letter] -= 1
            
                
