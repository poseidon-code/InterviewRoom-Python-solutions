# PROBLEM: Find length of loop in linked list
# https://practice.geeksforgeeks.org/problems/find-length-of-loop/1


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

def loop(head: Node, p: int):
    if head.next==None:
        return
    if p==-1:
        return

    tail, node = head, head
    while tail.next!=None:
        tail = tail.next
    for i in range(p):
        node = node.next
    
    tail.next = node


# SOLUTION
def length_loop(head: Node) -> int:
    if head==None or head.next==None:
        return 0

    slow, fast, entry = head, head, head

    while fast.next!=None and fast.next.next!=None:
        slow = slow.next
        fast = fast.next.next
        if slow==fast:
            result = 1
            while slow != entry:
                slow = slow.next
                entry = entry.next
                result+=1
            return result
    
    return 0


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
    loop(head, 4)

    # OUTPUT :
    length = length_loop(head)
    print(length)