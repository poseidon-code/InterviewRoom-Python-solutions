# PROBLEM: Next greater element
# https://leetcode.com/problems/next-greater-element-ii/
# https://practice.geeksforgeeks.org/problems/next-larger-element/0


from typing import List

# SOLUTION
def next_greater (nums: List[int]) -> List[int]:
    n = len(nums)
    stack = []
    result = [-1]*n

    for i in range(n*2) :
        while stack and (nums[stack[-1]] < nums[i%n]):
            result[stack.pop()] = nums[i%n]
        stack.append(i%n)
    
    return result


if __name__ == "__main__":
    # INPUT :
    nums = [1,2,3,4,3]

    # OUTPUT :
    print(next_greater(nums))