class Solution:
    def __init__(self):
        self.unfairness = float("inf")
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        children = [0]*k
        def dfs(curr,i):
            if i == len(cookies):
                potential = max(curr)
                self.unfairness = min(potential,self.unfairness)
                return
            for j in range(len(children)):
                children[j]+=cookies[i]
                if children[j] < self.unfairness:
                    dfs(children,i+1)
                children[j]-=cookies[i]
        dfs(children,0)
        return self.unfairness

    
        

