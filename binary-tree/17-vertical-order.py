# PROBLEM: Vertical order traversal
# https://www.interviewbit.com/problems/vertical-order-traversal-of-binary-tree/


from collections import defaultdict
from typing import DefaultDict, List


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
m = defaultdict(list)
def traverse (root: Node, x: int=0, y: int=0):
    if root!=None:
        traverse(root.left, x-1, y+1)
        traverse(root.right, x+1, y+1)
        m[x].append([y,root.data])

def vertical (root: Node) -> List[List[int]]:
    traverse(root, 0, 0)
    
    return [
        [ n for y, n in sorted(values) ]
        for x, values in sorted(m.items())
    ]


if __name__ == "__main__":
    # INPUT :
    elements = [1,2,3,4,5,6,7]
    root = NBT(elements, Node(elements[0]), 0, len(elements))

    # OUTPUT :
    print(vertical(root))