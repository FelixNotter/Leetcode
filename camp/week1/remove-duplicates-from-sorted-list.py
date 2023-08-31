# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node
        dummy = tail = ListNode(math.inf)
        track = head
        while track:
            if tail.val != track.val:
                tail.next = track
                tail = tail.next
            track = track.next
        tail.next = None
        return dummy.next