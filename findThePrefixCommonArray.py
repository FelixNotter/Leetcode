class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        prefix = set()
        common = [0]*n
        total = 0
        for r in range(n):
            if A[r] != B[r]:
                if A[r] in prefix:
                    total +=1  
                if B[r] in prefix:
                    total+=1
                common[r] = total
            else:
                total+=1
                common[r] = total      
            prefix.add(A[r])
            prefix.add(B[r])
        return common
