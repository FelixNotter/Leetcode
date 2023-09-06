# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #Get middle of linked list
        middle = self.get_mid(head) 
        #Reverse half of Link List
        second = self.reverse(middle)
        maxSoFar = -1
        first = head
        #start adding both and keep track of the max Sum so Far
        while first and second:
            currentSum = first.val + second.val
            maxSoFar = max(maxSoFar,currentSum)
            first = first.next
            second = second.next
        #return the maxSoFar
        return maxSoFar

    def get_mid(self,node):
        fast = node
        slow = node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverse(self,node):
        prev = None
        current = node
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev
        
