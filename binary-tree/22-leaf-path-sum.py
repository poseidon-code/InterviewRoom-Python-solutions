# PROBLEM: Maximum path sum between two leaf nodes
# https://www.codingninjas.com/codestudio/problems/maximum-path-sum-between-two-leaves_794950

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

def traverse (root: Node, result: int) -> int:
    if root==None : return 0
    if not root.left and not root.right : return root.data
    
    ls = traverse(root.left, result)
    rs = traverse(root.right, result)

    if root.left!=None and root.right!=None:
        result = max(result, ls+rs+root.data)
        return max(ls, rs) + root.data
    
    return rs+root.data if not root.left else ls+root.data

def leaf_path_sum (root: Node) -> int:
    result = INT_MIN
    v = traverse(root, result)

    if result==INT_MIN : return v
    return result


if __name__ == "__main__":
    # INPUT :
    elements = [1,2,3]
    root = NBT(elements, Node(elements[0]), 0, len(elements))

    # OUTPUT :
    print(leaf_path_sum(root))