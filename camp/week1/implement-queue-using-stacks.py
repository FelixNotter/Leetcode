class MyQueue:

    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        self.reverse()
        ans = self.stack.pop()
        self.reverse()
        return ans
    def peek(self) -> int:
        self.reverse()
        ans = self.stack[-1]
        self.reverse()
        return ans

    def empty(self) -> bool:
        return len(self.stack) == 0
        
    def reverse(self):
        l = 0 
        r = len(self.stack) - 1
        while l < r:
            self.stack[l],self.stack[r] = self.stack[r],self.stack[l]
            l+=1
            r-=1

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()