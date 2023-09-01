class Node:
    def __init__(self,val=0):
        self.val = val
        self.next = None
    
class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        i = 0
        cur = self.head
        while cur:
            if i == index:
                return cur.val
            i+=1
            cur = cur.next
        return -1
        

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newNode
        

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = Node(val)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            cur = self.head
            for i in range(index-1):
                if cur:cur = cur.next
            if cur:
                newNode.next = cur.next
                cur.next = newNode     

        

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return 
        if index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            for i in range(index-1):
                if cur:cur = cur.next
            if cur and cur.next:
                cur.next = cur.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)