# PROBLEM: Intersection point in Y shaped linked list
# https://leetcode.com/problems/intersection-of-two-linked-lists/
# https://www.interviewbit.com/problems/intersection-of-linked-lists/


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

def createY(headA: Node, headB: Node, skipA: int, skipB: int):
    pA = headA
    pB = headB
    for _ in range(1, skipA):
        pA = pA.next
    for _ in range(1, skipB):
        pB = pB.next
    pB.next = pA.next


# SOLUTION
def intersection(headA: Node, headB: Node) -> Node:
    pA = headA
    pB = headB

    if (pA == None or pB == None):
        return None

    while pA!=None and pB!=None and pA!=pB:
        pA = pA.next
        pB = pB.next

        if (pA == pB):
            return pA
        if (pA == None):
            pA = headB
        if (pB == None):
            pB = headA

    return pA;
    

if __name__ == "__main__":
    # INPUT :
    llA = LinkedList()
    llB = LinkedList()
    llA.add(4); llA.add(1); llA.add(8); llA.add(4); llA.add(5);
    llB.add(5); llB.add(6); llB.add(1); llB.add(8); llB.add(4); llB.add(5);
    headA = llA.get_head()
    headB = llB.get_head()

    # OUTPUT :
    createY(headA, headB, 2, 3)
    intersected = intersection(headA, headB)
    print("Intersected at", intersected.data)