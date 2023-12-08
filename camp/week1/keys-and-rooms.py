class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        adj = defaultdict(list)
        for i in range(len(rooms)):
            adj[i].extend(rooms[i])
        print(adj)
        queue = deque([0])
        visit = set([0])
        place = [False]*n
        place[0] = True
        while queue:
            node = queue.popleft()
        
           
            place[node] = True
            visit.add(node)
            for nei in adj[node]:
                if nei not in visit:
                    queue.append(nei)
                    visit.add(nei)
        for val in place:
            if not val:
                return False
        return True


        