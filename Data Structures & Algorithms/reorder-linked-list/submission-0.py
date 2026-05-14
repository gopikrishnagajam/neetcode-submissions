# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def reverse(head):
            prev = None
            current  = head
            while current:
                temp = current
                current = current.next
                temp.next = prev
                prev =temp
            return prev

        if not head or not head.next or not head.next.next:
            return 
        fast = head.next
        slow = head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        l2 =slow.next
        slow.next = None
        l1 = head

        l2 = reverse(l2)

        p1 = l1
        p2 = l2
        while p1 and p2:
            temp = p1
            p1 = p1.next
            temp.next =p2
            temp =p2
            p2 = p2.next
            temp.next =p1
        return 


        
