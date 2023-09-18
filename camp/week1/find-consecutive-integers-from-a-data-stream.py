class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.odd = 0
        self.val = value
        self.k = k
        

    def consec(self, num: int) -> bool:
        if num != self.val:
            self.odd+=1
        self.queue.append(num)
        if len(self.queue) > self.k:
            front= self.queue.popleft()
            if front != self.val:
                self.odd -=1
        return self.odd == 0 and len(self.queue) == self.k


        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)