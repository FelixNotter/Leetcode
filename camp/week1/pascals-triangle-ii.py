class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def dfs(row):
            if row == 0:
                return [1]
            local = [1]
            ans = dfs(row-1)
            for i in range(len(ans)-1):
                local.append(ans[i]+ans[i+1])
            local+=[1]
            return local
        return dfs(rowIndex)


            
            
        