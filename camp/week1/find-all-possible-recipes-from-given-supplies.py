class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        incoming  = defaultdict(int)
        adj = defaultdict(list)
        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                adj[ingredients[i][j]].append(recipes[i])
                incoming[recipes[i]]+=1
     
        queue = deque(supplies)
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for nei in adj[node]:
                incoming[nei]-=1
                if incoming[nei] == 0:
                    queue.append(nei)
        ans = []
        recipes = set(recipes)
        for rec in res:
            if rec in recipes:
                ans.append(rec)
        return ans



        