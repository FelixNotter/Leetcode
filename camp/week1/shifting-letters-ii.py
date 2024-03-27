class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefixSum = [0]*(len(s)+1)
        k = 1 
        for start,end,direct in shifts:
            if direct:
                prefixSum[start] +=1
                prefixSum[end+1] -= 1
            else:
                prefixSum[start] -=1
                prefixSum[end+1] += 1
        count = 0
        for i in range(len(prefixSum)):
            count += prefixSum[i]
            prefixSum[i] = count
    
       
        res=[]
        for i in range(len(prefixSum)-1):
            new_character_index = ((ord(s[i])-ord("a"))+prefixSum[i])%26
            adding = new_character_index + ord("a")
            char = chr(adding)
            res.append(char)
        return "".join(res)


"""
backword: -1 
forward: +1 

a, b, c
<---
^.  ^   --->
------>
0 +1  +2

1 2 3 5 6 7 
  _______

1 1
0 0 0 0 0 0
  _______

"""