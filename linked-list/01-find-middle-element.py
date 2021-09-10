# SOLUTION: Find middle element
# https://leetcode.com/problems/middle-of-the-linked-list/
# https://practice.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, n: Node):
        node = Node(n)
        if self.head:
            tail = self.head
            while tail.next!=None:
                tail=tail.next

            tail.next = node
        else:
            self.head = node

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
def middle_node(head: Node) -> Node:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


if __name__ == "__main__":
    # INPUT :
    ll = LinkedList()
    ll.add(0)
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.add(5)
    ll.add(6)
    ll.add(7)
    ll.add(8)
    head = ll.get_head()

    # OUTPUT :
    start = middle_node(head)
    ll.print_ll(start)