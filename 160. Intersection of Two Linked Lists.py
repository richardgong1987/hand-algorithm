from  typing import Optional

from utils.ListNode import ListNode, createListNode


class Solution:
    def getListLen(self, ls: ListNode):
        if not ls:
            return 0

        return 1 + self.getListLen(ls.next)

    def getIntersectionNode(self, A: ListNode, B: ListNode) -> Optional[ListNode]:
        ## (1). get length of list

        A_len, B_len = self.getListLen(A), self.getListLen(B)

        a_pointer = A
        b_pointer = B

        ##(2) move pointer

        if B_len > A_len:
            for _ in range(B_len - A_len):
                b_pointer = b_pointer.next
        else:
            for _ in range(A_len - B_len):
                a_pointer = a_pointer.next

        ## (3) compare

        while a_pointer != b_pointer:
            a_pointer = a_pointer.next
            b_pointer = b_pointer.next

        return a_pointer