class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        prefix = [0]*len(shifts)
        count = 0
        for i in range(len(shifts)-1,-1,-1):
            count += shifts[i]
            prefix[i] = count
        res = []
        for i in range(len(prefix)):
            new_character_index = ((ord(s[i])-ord("a"))+prefix[i])%26
            adding = new_character_index + ord("a")
            char = chr(adding)
            res.append(char)
        return "".join(res)


            
