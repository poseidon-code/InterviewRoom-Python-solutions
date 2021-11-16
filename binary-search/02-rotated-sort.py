# PROBLEM: Serach in a rotated sorted array
# https://leetcode.com/problems/search-in-rotated-sorted-array/
# https://www.interviewbit.com/problems/rotated-sorted-array-search/
# https://practice.geeksforgeeks.org/problems/search-in-a-rotated-array/0


from typing import List

# SOLUTION
def search_rotated (nums: List[int], target: int) -> int: 
    n = len(nums)
    l, h = 0, n-1

    while l<h:
        m = int((l+h)/2)
        if nums[m]>nums[h] : l = m+1
        else : h = m

    rot=l
    l=0
    h=n-1
    while l<=h:
        m = int((l+h)/2)
        rm = (m+rot)%n
        if nums[rm]==target : return rm
        if nums[rm]<target : l = m+1
        else : h = m-1

    return -1


if __name__ == "__main__":
    # INPUT :
    nums = [4,5,6,7,0,1,2]
    target = 0

    # OUTPUT :
    print(search_rotated(nums, target))