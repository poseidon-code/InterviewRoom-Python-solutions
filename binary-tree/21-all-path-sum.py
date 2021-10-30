# PROBLEM: All Root to Leaf path sum
# https://leetcode.com/problems/path-sum-ii/
# https://www.interviewbit.com/problems/root-to-leaf-paths-with-sum/

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
def traverse (root: Node, target: int, path: List[int], paths: List[List[int]]):
    if root==None : return
    path.append(root.data)

    if not root.left and not root.right and target==root.data:
        paths.append(path[:])
    else:
        traverse(root.left, target - root.data, path, paths)
        traverse(root.right, target - root.data, path, paths)
    
    path.pop()

def all_path_sum (root: Node, target: int) -> List[List[int]]:
    paths = []
    path = []

    traverse(root, target, path, paths)
    return paths

if __name__ == "__main__":
    # INPUT :
    elements = [1,2,2]
    target = 3
    root = NBT(elements, Node(elements[0]), 0, len(elements))

    # OUTPUT :
    print(all_path_sum(root, target))