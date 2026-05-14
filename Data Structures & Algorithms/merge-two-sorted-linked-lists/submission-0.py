# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1,l2 = list1,list2
        head =ListNode(0)
        pt =head
        while l1 and l2:
            if l1.val<= l2.val:
                pt.next =l1
                l1 =l1.next
                pt =pt.next
            else:
                pt.next =l2
                l2 = l2.next
                pt =pt.next
        if not l1:
            pt.next =l2
        if not l2:
            pt.next = l1
        return head.next
                