# PROBLEM: Reverse a linked list
# https://leetcode.com/problems/reverse-linked-list/
# https://www.interviewbit.com/problems/reverse-linked-list/


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, n: Node):
        t = Node(n)
        if self.head:
            tail = self.head
            while tail.next!=None:
                tail=tail.next

            tail.next = t
        else:
            self.head = t

    def print_ll(self, start: Node):
        p = start
        print("[", end='')
        while p!=None:
            print(p.data, end=" ")
            p=p.next
        print("\b]")

    def get_head(self) -> Node:
        return self.head


# SOLUTION
def reverse(head: Node) -> Node:
    c = None
    while head:
        n = head.next
        head.next = c
        c = head
        head = n
    return c


if __name__ == "__main__":
    # INPUT :
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.add(5)
    ll.add(6)
    head = ll.get_head()

    # OUTPUT :
    reversed = reverse(head)
    ll.print_ll(reversed)