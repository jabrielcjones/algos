#! /usr/bin/env python

# Definition for doubly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.prev = prev
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.curr = None

    def add(self, val):
        new_node = ListNode(val)

        if self.head is None:
            self.head = new_node

        if self.curr is not None:
            self.curr.next = new_node
            new_node.prev = self.curr

        self.curr = new_node

        # print('Current is {0}'.format(self.curr.val))
        # if self.curr.prev:
        #   print('Previous is {0}'.format(self.curr.prev.val))

        # else:
        #   print('Previous is None')


    def print_list(self):
        curr = self.head

        llist = ''
        while curr != None:
            llist += '<- {0} -> '.format(curr.val)
            curr = curr.next

        print(llist)

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = LinkedList()
        self.history.add(homepage)

    def visit(self, url: str) -> None:
        self.history.add(url)

    def back(self, steps: int) -> str:
        
        for i in range(0, steps):
            if self.history.curr.prev is None:
                break

            else:
                self.history.curr = self.history.curr.prev

        return self.history.curr.val

    def forward(self, steps: int) -> str:

        for i in range(0, steps):
            if self.history.curr.next is None:
                break

            else:
                self.history.curr = self.history.curr.next

        return self.history.curr.val
   
    def display(self):
        self.history.print_list()

        
if __name__ == "__main__":

    # Your BrowserHistory object will be instantiated and called as such:
    homepage = 'www.google.com'
    b_history = BrowserHistory(homepage)
    b_history.display()

    url = 'www.yahoo.com'
    b_history.visit(url)
    b_history.display()

    url = 'www.nfl.com'
    b_history.visit(url)
    b_history.display()

    url = 'www.wikipedia.com'
    b_history.visit(url)
    b_history.display()

    url = 'www.github.com'
    b_history.visit(url)
    b_history.display()

    steps = 2
    curr_url = b_history.back(steps)
    b_history.display()
    print('Steps Back: {0}'.format(steps))
    print('Current: {0}'.format(curr_url))

    steps = 0
    curr_url = b_history.forward(steps)
    b_history.display()
    print('Steps Forward: {0}'.format(steps))
    print('Current: {0}'.format(curr_url))

    url = 'www.aws.com'
    b_history.visit(url)
    b_history.display()
