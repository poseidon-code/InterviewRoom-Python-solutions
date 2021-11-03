# PROBLEM: Minimum distance between two nodes
# https://practice.geeksforgeeks.org/problems/min-distance-between-two-given-nodes-of-a-binary-tree/1

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


def lca (root: Node, p: Node, q: Node) -> Node:
    if not root or root==p or root==q : return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    return right if not left else left if not right else root

def traverse (root: Node, a: Node) -> int:
    if not root : return 0
    if root.data==a.data : return 1
    c = traverse(root.left, a)
    d = traverse(root.right, a)
    if not c and not d : return 0
    else : return c+d+1


# SOLUTION
def distance (root: Node, p: Node, q: Node) -> int:
    n = lca(root, p, q)

    c = traverse(n, p)
    d = traverse(n, q)

    return c+d-2


if __name__ == "__main__":
    # INPUT :
    elements = [3,5,1,6,2,0,8,None,None,7,4]
    root = NBT(elements, Node(elements[0]), 0, len(elements))
    p = root.left
    q = root.right

    # OUTPUT :
    print(distance(root, p, q))