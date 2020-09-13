#! /usr/bin/env python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = ListNode(val)

        new_node.next = self.head

        self.head = new_node
        
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    return getTotalList(sumList(l1) + sumList(l2))
    # total = str(sumList(l1) + sumList(l2))
    # total = str(getNum(l1) + getNum(l2))

    # ll = LinkedList()
    # for c in total:
    #     ll.push(int(c))

    # return ll.head

def sumList(l: ListNode):
    # 342
    # 3 * 10^2 + 4 * 10^1 + 2 * 10^0

    l_sum, place = 0, 0 
    current = l

    while True:
        l_sum += current.val * pow(10, place)

        if not current.next:
            break

        current = current.next
        place += 1

    return l_sum

def getNum(l: ListNode):
    current = l
    num = ""

    while True:
        num += str(current.val)

        if not current.next:
            break

        current = current.next

    return int(num[::-1])

def getTotalList(total: int):
    # 804

    length = len(str(total))

    ll = LinkedList()
    for place in range(length - 1, -1, -1):
        num = int(total / pow(10, place))

        ll.push(num)

        total -= num * pow(10, place)

    return ll.head

if __name__ == "__main__":
    # 342
    # 2 > 4 > 3
    l1 = LinkedList()
    l1.push(3)
    l1.push(4)
    l1.push(2)

    # 462
    # 2 > 6 > 4
    l2 = LinkedList()
    l2.push(4)
    l2.push(6)
    l2.push(2)

    addTwoNumbers(l1.head, l2.head)
