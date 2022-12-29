import typing

from utils.ListNode import ListNode, createListNode


class Solution:
    def reverse(self, ll: ListNode) -> ListNode:
        pre = None
        cur = ll

        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        return pre

    def reorderList(self, head: typing.Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow = head
        fast = head.next

        ##(1) fist step find middle node

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        ##(2) splite it to two list
        leftNode = head
        rightNode = slow.next
        slow.next = None

        ##(3) reverse rightNode
        rightNode = self.reverse(rightNode)

        ## tmp
        dummy = ListNode()
        result = dummy

        while leftNode is not None or rightNode is not None:

            if leftNode is not None:
                result.next = leftNode
                result = result.next
                leftNode = leftNode.next

            if rightNode is not None:
                result.next = rightNode
                result = result.next
                rightNode = rightNode.next

        print(dummy)


node = createListNode([1, 2, 3, 4, 5])
solution = Solution()
solution.reorderList(node)
