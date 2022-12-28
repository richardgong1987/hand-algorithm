class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head

        while cur is not None:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        return pre

