# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = tail = ListNode()
        i = 0
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            i+=1
            if i%k == 0:
                tail.next = prev
                while tail.next:
                    tail = tail.next
                prev = None
        back = None
        rev = prev
        while rev:
            nxt = rev.next
            rev.next = back
            back = rev
            rev = nxt
        tail.next = back
        return dummy.next


        