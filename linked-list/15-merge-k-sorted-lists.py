# PROBLEM: Merge k sorted lists
# https://leetcode.com/problems/merge-k-sorted-lists/
# https://www.interviewbit.com/problems/merge-two-sorted-lists/
# https://practice.geeksforgeeks.org/problems/merge-k-sorted-linked-lists/1


from typing import List
from queue import PriorityQueue


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
def merge_sorted (lists: List[Node]) -> Node:
    heap = PriorityQueue()
    head = Node(None)
    c = head

    for i, node in enumerate(lists):
        if node:
            heap.put((node.data, i, node))

    while heap.qsize()>0:
        t = heap.get()
        c.next, i = t[2], t[1]
        c = c.next
        if c.next:
            heap.put((c.next.data, i, c.next))
    
    return head.next



if __name__ == "__main__":
    # INPUT :
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll3 = LinkedList()
    ll1.add(1)
    ll1.add(4)
    ll1.add(5)
    ll2.add(1)
    ll2.add(3)
    ll2.add(4)
    ll3.add(2)
    ll3.add(6)
    h1 = ll1.get_head()
    h2 = ll2.get_head()
    h3 = ll3.get_head()

    lists = [h1, h2, h3]

    # OUTPUT :
    result = merge_sorted(lists)
    ll1.print_ll(result)