# PROBLEM: Remove nth node from the end
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# https://www.interviewbit.com/problems/remove-nth-node-from-list-end/



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
def remove_nth(head: Node, n: int) -> Node:
    slow = head
    fast = head

    for i in range(n+1):
        fast = fast.next
    
    while fast != None:
        slow = slow.next
        fast = fast.next
    
    slow.next = slow.next.next

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
    head = ll.get_head()

    # OUTPUT :
    new_head = remove_nth(head, 2)
    ll.print_ll(new_head)