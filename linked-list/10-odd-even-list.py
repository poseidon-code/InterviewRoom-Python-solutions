# PROBLEM: Segregate even and odd positioned nodes in linked list
# https://leetcode.com/problems/odd-even-linked-list/
# https://practice.geeksforgeeks.org/problems/rearrange-a-linked-list/1


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
def oddeven(head: Node) -> Node:
    if head==None or head.next==None:
        return head

    odd, even = head, head.next

    if (even.next==None):
        return head
    
    c, e = even.next, even

    while c!=None:
        odd.next = c
        e.next = c.next
        odd = odd.next
        e = e.next

        if e!=None:
            c = e.next
        else:
            break
    
    odd.next = even
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
    result = oddeven(head)
    ll.print_ll(result)