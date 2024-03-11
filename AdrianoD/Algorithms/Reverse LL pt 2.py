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
            curr = head
            last = None
            while curr:
                new_head = ListNode(curr.val)
                if last != None:
                    new_head.next = last
                last = new_head
                curr = curr.next
        return new_head
            
            
                
s = Solution()
linkedList = ListNode(1, ListNode(2, ListNode(3)))
s.reverseList(linkedList)
                