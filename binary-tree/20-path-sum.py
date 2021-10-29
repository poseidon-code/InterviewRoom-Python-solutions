# PROBLEM: Path sum
# https://www.interviewbit.com/problems/path-sum/
# https://leetcode.com/problems/path-sum/


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
def has_path_sum (root: Node, target: int) -> bool:
    if root==None : return False

    if root.left == root.right : return target == root.data

    return has_path_sum(root.left, target - root.data) or has_path_sum(root.right, target - root.data)


if __name__ == "__main__":
    # INPUT :
    elements = [1,2,3]
    target = 3
    root = NBT(elements, Node(elements[0]), 0, len(elements))

    # OUTPUT :
    print(has_path_sum(root, target))