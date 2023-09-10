class Node:
    def __init__(self,val = 0):
        self.val = val
        self.next = None

class MyStack:

    def __init__(self):
        self.sentinel = Node()

    def push(self, x: int) -> None:
        newNode = Node(x)
        newNode.next = self.sentinel.next
        self.sentinel.next = newNode
        

    def pop(self) -> int:
        node = self.sentinel.next
        self.sentinel.next = node.next
        return node.val
        

    def top(self) -> int:
        return self.sentinel.next.val
        

    def empty(self) -> bool:
        return not self.sentinel.next
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()