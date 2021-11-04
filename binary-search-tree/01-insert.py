# PROBLEM: Insert Node into binary search tree
# https://leetcode.com/problems/insert-into-a-binary-search-tree/


class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def NBT (elements, root, i, n) -> Node:
    if n==0 : return None

    if i<n:
        temp = Node(elements[i])
        root = temp
        root.left = NBT(elements, root.left, 2*i+1, n)
        root.right = NBT(elements, root.right, 2*i+2, n)

    return root


# SOLUTION
def insert (root: Node, value: int) -> Node:
    if not root : return Node(value)
    c = root
    while c:
        if c.data < value:
            if c.right : c = c.right
            else:
                c.right = Node(value)
                break
        else:
            if c.left : c = c.left
            else:
                c.left = Node(value)
                break
    return root


if __name__ == "__main__":
    # INPUT :
    elements = [4,2,7,1,3]
    value = 5
    root = NBT(elements, Node(elements[0]), 0, len(elements))

    # OUTPUT :
    insert(root, value)