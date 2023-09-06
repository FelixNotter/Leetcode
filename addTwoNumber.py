# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        carry = 0
        h1 = l1
        h2 = l2
        while h1 or h2 or carry:
            v1 = h1.val if h1 else 0
            v2 = h2.val if h2 else 0
            
            num = (v1+v2 + carry)%10
            print(num)
            carry = (v1+v2+carry)//10
            newNode = ListNode(num)
            tail.next = newNode
            tail = newNode
            if h1:
                h1 = h1.next
            if h2:
                h2 = h2.next
        return dummy.next
