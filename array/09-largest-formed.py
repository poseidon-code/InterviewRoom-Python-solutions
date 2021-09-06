# PROBLEM: Largest number formed from an array
# https://leetcode.com/problems/largest-number/
# https://www.interviewbit.com/problems/largest-number/
# https://practice.geeksforgeeks.org/problems/largest-number-formed-from-an-array/0


from typing import List
from functools import cmp_to_key


# SOLUTION
def largest_formed (nums: List[int]) -> str:
    s = list(map(str, nums))

    comp = lambda a, b: -1 if a+b>b+a else (1 if a+b<b+a else 0)
    s = sorted(s, key=cmp_to_key(comp))

    result = str(int(''.join(s)))

    return result


if __name__ == "__main__":
    # INPUT :
    nums = [3,30,34,5,9]

    # OUTPUT :
    print(largest_formed(nums))