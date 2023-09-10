class Node:
    def __init__(self,val=-1):
        self.val = val
        self.prev = None
        self.next = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.dummy = Node()
        self.tail = self.dummy
        self.size = k
        self.len = 0

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            newNode = Node(value)
            newNode.next = self.dummy.next
            newNode.prev = self.dummy
            node = self.dummy.next
            if node:
                node.prev = newNode
            self.dummy.next = newNode
            
            if self.tail == self.dummy:
                self.tail = newNode
            self.len+=1
            return True
        return False
        
    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            newNode = Node(value)
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
            self.len+=1
            return True
        return False

    def deleteFront(self) -> bool:
        if not self.dummy.next:
            return False
        node = self.dummy.next
        if node == self.tail:
            self.tail = node.prev
        node.prev = None
        nxt = node.next
        node.next = None
        if nxt:
            nxt.prev = self.dummy
        self.dummy.next = nxt
        self.len -= 1
        return True

    def deleteLast(self) -> bool:
        if self.tail == self.dummy:
            return False
        prev = self.tail.prev
        self.tail.prev = None
        self.tail = prev
        self.tail.next = None
        self.len-=1  
        return True

    def getFront(self) -> int:
        return self.dummy.next.val if self.dummy.next else -1

    def getRear(self) -> int:
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.len == 0
    
    def isFull(self) -> bool:
        return self.size  == self.len
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
