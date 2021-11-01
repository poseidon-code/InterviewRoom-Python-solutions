# PROBLEM: Maximum path sum from any node to node
# https://leetcode.com/problems/binary-tree-maximum-path-sum/


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
INT_MIN = -2**32
max_sum = INT_MIN

def traverse (root: Node) -> int:
    if root==None : return 0
    c = 0 if root.data==None else root.data
    
    ls = max(traverse(root.left),0)
    rs = max(traverse(root.right),0)

    global max_sum
    max_sum = max(max_sum, ls+rs+c)
    return max(ls, rs) + c

def node_path_sum (root: Node) -> int:
    v = traverse(root)

    global max_sum
    if max_sum==INT_MIN : return v
    return max_sum


if __name__ == "__main__":
    # INPUT :
    elements = [-10,9,20,None,None,15,7]
    root = NBT(elements, Node(elements[0]), 0, len(elements))

    # OUTPUT :
    print(node_path_sum(root))