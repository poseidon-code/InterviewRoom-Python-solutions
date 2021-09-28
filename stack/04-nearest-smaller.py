# PROBLEM: Nearest smaller
# https://www.interviewbit.com/problems/nearest-smaller-element/


from typing import List


# SOLUTION
def nearest_smaller (nums: List[int]) -> List[int]:
    result = [-1]
    stack = [nums[0]]

    for i in range(1, len(nums)):
        while len(stack)!=0 and stack[-1] >= nums[i]:
            stack.pop()
        
        if len(stack)==0:
            result.append(-1)
        else:
            result.append(stack[-1])
        stack.append(nums[i])

    return result


if __name__ == "__main__":
    # INPUT :
    nums = [4,5,2,10,8]

    # OUTPUT :
    print(nearest_smaller(nums))