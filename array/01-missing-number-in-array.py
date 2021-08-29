# PROBLEM: Missing number in array
# https://leetcode.com/problems/missing-number/
# https://practice.geeksforgeeks.org/problems/missing-number-in-array/0

from typing import List

# SOLUTION
def missing_number(nums: List[int]) -> int:
    result = len(nums)
    i=0

    for num in nums:
        result = result^num^i
        i+=1

    return result


if __name__ == '__main__':
    # INPUT :
    nums = [3,2,0,1]

    # OUTPUT :
    print(missing_number(nums))