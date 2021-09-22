# PROBLEM: Delete N nodes after M nodes of a linked list
# https://practice.geeksforgeeks.org/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/1


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
def delete_nodes (head: Node, m: int, n: int) -> Node:
    c= head
    t: Node = None

    while c!=None:
        for i in range(1, m):
            if c!=None:
                c = c.next
        
        if c==None:
            return head

        t = c.next
        for count in range(1, n+1):
            if t!=None:
                t=t.next

        c.next = t
        c=t
    
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
    result = delete_nodes(head, 2, 5)
    ll.print_ll(result)