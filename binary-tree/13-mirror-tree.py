# PROBLEM: Convert binary tree to its mirror tree
# https://practice.geeksforgeeks.org/problems/mirror-tree/1


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
def mirror (root: Node):
    if root==None : return
    else:
        t = Node()
        mirror(root.left)
        mirror(root.right)
        t = root.left
        root.left = root.right
        root.right = t


if __name__ == "__main__":
    # INPUT :
    elements = [1,3,2,None,None,5,4]
    root = NBT(elements, Node(elements[0]), 0, len(elements))

    # OUTPUT :
    mirror(root)