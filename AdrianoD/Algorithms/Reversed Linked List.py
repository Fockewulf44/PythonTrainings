# Definition for singly-linked list.
from typing import Union, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None or head.next == None:
            return head
        else:
            i = 0
            ln = []
            next1 = head
            reverse = ListNode()
            while next1 != None:
                ln.append(next1.val)
                next1 = next1.next
                i += 1

            y = len(ln) - 1

            first = ListNode()
            first.val = ln[y]
            reverse = first
            y = y - 1
            while y > -1:
                reverse.next = ListNode()
                reverse.next.val = ln[y]
                reverse = reverse.next
                y -= 1
            else:
                return first

    linkedList = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    s = Solution
    result = s.reverseList(s, linkedList)
    print(result)
