# PROBLEM: Reverse list in a group of given size k
# https://leetcode.com/problems/reverse-nodes-in-k-group/
# https://www.interviewbit.com/problems/k-reverse-linked-list/


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
def reverse(first: Node, last: Node):
    p = last
    while first!=last:
        t = first.next
        first.next = p
        p = first
        first = t
    return p

def reverse_group(head: Node, k: int) -> Node:
    node = head

    for i in range(k):
        if node==None:
            return head
        node = node.next

    new_head = reverse(head, node)
    head.next = reverse_group(node, k)

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
    reversed = reverse_group(head, 2)
    ll.print_ll(reversed)