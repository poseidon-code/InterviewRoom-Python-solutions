# PROBLEM: Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


from typing import List

# SOLUTION
def search_range (nums: List[int], target: int) -> List[int]: 
    i, j = 0, len(nums)-1
    result = [-1,-1]

    while i<j:
        mid = int((i+j)/2)
        if (nums[mid]<target) : i = mid+1
        else : j = mid
    if nums[i] != target : return result
    else : result[0] = i

    j = len(nums)-1
    while i<j:
        mid = int((i+j)/2 + 1)
        if nums[mid]>target : j = mid-1
        else : i = mid
    result[1] = j
    
    return result


if __name__ == "__main__":
    # INPUT :
    nums = [5,7,7,8,8,10]
    target = 8

    # OUTPUT :
    print(search_range(nums, target))