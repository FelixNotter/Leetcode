# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        evenHead = even= ListNode()
        oddHead  = odd = ListNode()
        current = head
        count = 1
        while current:
            if count % 2 != 0:
                odd.next = current
                odd = odd.next
            else:
                even.next = current
                even = even.next
            current = current.next
            count +=1
        odd.next = None
        even.next = None
        odd.next = evenHead.next
        return oddHead.next

