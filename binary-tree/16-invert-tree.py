# PROBLEM: Invert a binary tree
# https://leetcode.com/problems/invert-binary-tree/
# https://www.interviewbit.com/problems/invert-the-binary-tree/


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
def invert (root: Node) -> Node:
    s = []
    s.append(root)

    while len(s)!=0:
        p = s.pop()

        if (p!=None):
            s.append(p.left)
            s.append(p.right)
            p.left, p.right = p.right, p.left
        
    return root


if __name__ == "__main__":
    # INPUT :
    elements = [4,2,7,1,3,6,9]
    root = NBT(elements, Node(elements[0]), 0, len(elements))

    # OUTPUT :
    invert(root)