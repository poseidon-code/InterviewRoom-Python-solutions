# PROBLEM: Find minimum in a rotated sorted array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List

# SOLUTION
def minimum (nums: List[int]) -> int: 
    start, end = 0, len(nums)-1
    
    while start<end:
        if nums[start]<nums[end]:
            return nums[start]
        
        mid = int((start+end)/2)

        if nums[mid]>=nums[start] : start = mid+1
        else : end = mid

    return nums[start]


if __name__ == "__main__":
    # INPUT :
    nums = [3,4,5,1,2]

    # OUTPUT :
    print(minimum(nums))