# PROBLEM: Rotate a linked list
# https://leetcode.com/problems/rotate-list/
# https://www.interviewbit.com/problems/rotate-list/


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
def rotate(head: Node, k: int) -> Node:
    if head==None:
        return head

    l = 1
    new_head = tail = head

    while tail.next:
        tail = tail.next
        l+=1
    tail.next = head

    if k%l == k:
        for i in range(l-k):
            tail = tail.next
    
    new_head = tail.next
    tail.next = None

    return new_head


if __name__ == "__main__":
    # INPUT :
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.add(5)
    head = ll.get_head()

    # OUTPUT :
    rotated = rotate(head, 2)
    ll.print_ll(rotated)