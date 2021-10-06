# PROBLEM: Sliding window maximum
# https://leetcode.com/problems/sliding-window-maximum/
# https://www.interviewbit.com/problems/sliding-window-maximum/


from typing import Deque, List

# SOLUTION
def maximum (nums: List[int], k: int) -> List[int]:
    buffer = Deque()
    result = []

    for i in range(len(nums)):
        while (len(buffer)!=0 and nums[i]>=nums[buffer[-1]]):
            buffer.pop()
        buffer.append(i)

        if i>=k-1:
            result.append(nums[buffer[0]])
        if buffer[0]<=i-k+1:
            buffer.popleft()

    return result


if __name__ == "__main__":
    # INPUT :
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3

    # OUTPUT :
    print(maximum(nums, k))