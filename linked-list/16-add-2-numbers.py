# PROBLEM: Add two numbers
# https://leetcode.com/problems/add-two-numbers/
# https://www.interviewbit.com/problems/add-two-numbers-as-lists/


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
def add (l1: Node, l2: Node) -> Node:
    head = Node(0)
    t = head
    c = 0

    while c!=0 or l1!=None or l2!=None:
        if l1!=None:
            c += l1.data
            l1 = l1.next
        if l2!=None:
            c += l2.data
            l2 = l2.next

        t.next = Node(c%10)
        t = t.next
        c//= 10
    
    return head.next



if __name__ == "__main__":
    # INPUT :
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll1.add(2)
    ll1.add(4)
    ll1.add(3)
    ll2.add(5)
    ll2.add(6)
    ll2.add(4)
    h1 = ll1.get_head()
    h2 = ll2.get_head()

    # OUTPUT :
    result = add(h1, h2)
    ll1.print_ll(result)