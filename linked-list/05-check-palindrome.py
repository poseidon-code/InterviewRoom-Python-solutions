# PROBLEM: Check if a linked list is palindrome
# https://leetcode.com/problems/palindrome-linked-list/
# https://www.interviewbit.com/problems/palindrome-list/


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
def is_palindrome(head: Node) -> bool:
    rev = None
    slow = fast = head

    while fast and fast.next:
        t = rev
        fast = fast.next.next
        rev = slow
        slow = slow.next
        rev.next = t
    
    if fast:
        slow = slow.next

    while rev and rev.data == slow.data:
        slow = slow.next
        rev = rev.next
    
    return not rev


if __name__ == "__main__":
    # INPUT :
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(3)
    ll.add(2)
    ll.add(1)
    head = ll.get_head()

    # OUTPUT :
    print(is_palindrome(head))