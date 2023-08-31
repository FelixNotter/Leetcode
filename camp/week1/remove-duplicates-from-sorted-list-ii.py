# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()
        count = defaultdict(int)
        cur = head
        while cur:
            count[cur.val]+=1
            cur = cur.next
        print(count)
        cur2 = head
        while cur2:
            if count[cur2.val] == 1:
                tail.next = cur2
                tail = tail.next
            cur2 = cur2.next
        tail.next = None
        return dummy.next