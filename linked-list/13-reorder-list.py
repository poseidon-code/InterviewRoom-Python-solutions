# PROBLEM: Reorder list
# https://leetcode.com/problems/reorder-list/
# https://www.interviewbit.com/problems/reorder-list/


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
def reorder(head: Node) -> Node:
    if head==None or head.next==None:
        return head

    prev, slow, fast, l1, l2 = None, head, head, head, None

    while fast!=None and fast.next!=None:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = None

    p, c, n = None, slow, None
    while c!=None:
        n=c.next
        c.next=p
        p=c
        c=n
    l2 = p

    while l1!=None:
        n1, n2 = l1.next, l2.next
        l1.next = l2

        if n1==None:
            break

        l2.next=n1
        l1=n1
        l2=n2

    return head


if __name__ == "__main__":
    # INPUT :
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.add(5)
    ll.add(6)
    ll.add(7)
    ll.add(8)
    ll.add(9)
    head = ll.get_head()

    # OUTPUT :
    result = reorder(head)
    ll.print_ll(result)