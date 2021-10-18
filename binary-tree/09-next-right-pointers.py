# PROBLEM: Populating next right pointers
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/


class Node:
    def __init__(self, data=0, left=None, right=None, next=None):
        self.data = data
        self.left = left
        self.right = right
        self.next = next

def NBT (elements, root, i, n) -> Node:
    if n==0 : return None

    if i<n:
        temp = Node(elements[i])
        root = temp
        root.left = NBT(elements, root.left, 2*i+1, n)
        root.right = NBT(elements, root.right, 2*i+2, n)

    return root


# SOLUTION
def connect(root: Node):
    while root!=None and root.left!=None:
        c = root
        while c!=None:
            c.left.next = c.right
            c.right.next = c.next.left if c.next!=None else None
            c = c.next
        root = root.left


if __name__ == "__main__":
    # INPUT :
    elements = [1,2,3,4,5,6,7]
    root = NBT(elements, Node(elements[0]), 0, len(elements))

    # OUTPUT :
    connect(root)