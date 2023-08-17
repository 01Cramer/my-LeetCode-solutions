from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        curr_1 = list1
        curr_2 = list2

        merged_list = ListNode()
        curr_merged = merged_list

        while curr_1 is not None and curr_2 is not None:
            if curr_2 is None or curr_1.val <= curr_2.val:
                curr_merged.next = curr_1
                curr_1 = curr_1.next
            else:
                curr_merged.next = curr_2
                curr_2 = curr_2.next
            curr_merged = curr_merged.next

        if curr_1 is not None:
            curr_merged.next = curr_1
        else:
            curr_merged.next = curr_2

        return merged_list.next
