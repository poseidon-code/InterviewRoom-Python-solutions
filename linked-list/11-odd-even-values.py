# PROBLEM: Segregate even and odd valued nodes in a linked list 
# https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/


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
def oddeven_values(head: Node) -> Node:
    if head==None or head.next==None:
        return head

    es, ee, os, oe = None, None, None, None
    c = head

    while c!=None:
        val = c.data

        if val%2 == 0:
            if es==None:
                es = c
                ee = es
            else:
                ee.next = c
                ee = ee.next
        else:
            if os==None:
                os = c
                oe = os
            else:
                oe.next = c
                oe = oe.next
        
        c = c.next
    
    if os==None or es==None:
        return None

    ee.next = os
    oe.next = None

    return es


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
    result = oddeven_values(head)
    ll.print_ll(result)