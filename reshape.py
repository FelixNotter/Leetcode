class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        ROWS = len(mat)
        COLS = len(mat[0])
        print(ROWS,COLS)
        # if ROWS == r and COLS == c:
        #     return mat 
        if r != ROWS and r*c != ROWS*COLS:
            r = ROWS
        if c != COLS and r*c != ROWS*COLS:
            c = COLS
        ans = [[0]*c for i in range(r)]
        ptr1 = 0
        ptr2 = 0
        for i in range(r):
            for j in range(c):
                if ptr2 >= COLS:
                    ptr1+=1
                    ptr1 %= ROWS
                ptr2 = ptr2 % COLS
                print(ptr1,ptr2,c)
                ans[i][j] = mat[ptr1][ptr2]
                ptr2 += 1
            
        return ans 
