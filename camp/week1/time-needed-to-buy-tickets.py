class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tickets = [[False,tickets[i]] for i in range(len(tickets))]
        tickets[k][0] = True
        queue = deque(tickets)
        i = 0
        while True:
            flag,buy = queue.popleft()
            i+=1
            buy -=1
            if flag and not buy:
                break
            if buy:
                queue.append([flag,buy])
        return i
            
        
        