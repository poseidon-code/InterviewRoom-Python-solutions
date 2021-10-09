# PROBLEM: Maximum height of binary tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# https://www.interviewbit.com/problems/max-depth-of-binary-tree/


from typing import List

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
def maximum_height (root):
    return 0 if root==None else max(maximum_height(root.left), maximum_height(root.right) + 1)



if __name__ == "__main__":
    # INPUT :
    elements = [3,9,20,None,None,15,7]
    root = NBT(elements, Node(elements[0]), 0, len(elements))

    # OUTPUT :
    print(maximum_height(root))