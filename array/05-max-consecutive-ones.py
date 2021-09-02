# PROBLEM: Max consecutive ones
# https://leetcode.com/problems/max-consecutive-ones/
# https://www.interviewbit.com/problems/max-continuous-series-of-1s/


from typing import List

# SOLUTION
def max_ones(nums: List[int]) -> int:
    max1s=0
    count=0

    for n in nums:
        if n==1:
            count+=1
            max1s = max(count, max1s)
        else:
            count=0

    return max1s


if __name__ == "__main__":
    # INPUT :
    nums = [1,1,0,1,1,1]

    # OUTPUT :
    print(max_ones(nums))