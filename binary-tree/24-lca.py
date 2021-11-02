# PROBLEM: Least Common Ancestor of two nodes
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

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
def lca (root: Node, p: Node, q: Node) -> Node:
    if not root or root==p or root==q : return root

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    return right if not left else left if not right else root


if __name__ == "__main__":
    # INPUT :
    elements = [3,5,1,6,2,0,8,None,None,7,4]
    root = NBT(elements, Node(elements[0]), 0, len(elements))
    p = root.left
    q = root.right

    # OUTPUT :
    print(lca(root, p, q).data)