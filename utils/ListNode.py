from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createListNode(ls: List[int]) -> ListNode:
    p1 = ListNode()
    p2 = p1
    for _, val in enumerate(ls):
        p2.next = ListNode(val)
        p2 = p2.next

    return p1.next


def swap(a: ListNode, b: ListNode):
    a.val, b.val = b.val, a.val


def printListNode(ll:ListNode):
    while ll:
        print(ll.val, end='')
        ll = ll.next
