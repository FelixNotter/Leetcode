# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_less = tail_less =  ListNode()
        dummy_greater = tail_great = ListNode()
        cur = head
        while cur:
            if cur.val < x:
                tail_less.next = cur
                
                tail_less = tail_less.next
            else:
                tail_great.next = cur
                tail_great = tail_great.next
            cur = cur.next
        tail_less.next = None
        tail_great.next = None

        tail_less.next = dummy_greater.next
        return dummy_less.next