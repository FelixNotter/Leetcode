# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        answer = [0]*self.getLen(head)
        cur = head
        stack = []
        i = 0
        while cur:
            while stack and stack[-1][1] < cur.val:
                idx,val = stack.pop()
                answer[idx] = cur.val
            stack.append((i,cur.val))
            i+=1
            cur = cur.next
        return answer
        
    def getLen(self,head):
        i = 0
        cur = head
        while cur:
            i+=1
            cur = cur.next
        return i
        
