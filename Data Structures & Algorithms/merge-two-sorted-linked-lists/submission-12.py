# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr_one = list1
        curr_two = list2

        tmp = ListNode(-1)
        start = tmp

        while curr_one and curr_two:
            if curr_one.val < curr_two.val:
                tmp.next = curr_one
                curr_one = curr_one.next
            else:
                tmp.next = curr_two
                curr_two = curr_two.next
            tmp = tmp.next
        
        # Check if either curr_one or two isn't null, tack it on
        while curr_one:
            tmp.next = curr_one
            curr_one = curr_one.next
            tmp = tmp.next
        
        while curr_two:
            tmp.next = curr_two
            curr_two = curr_two.next
            tmp = tmp.next

        # Return
        return start.next

