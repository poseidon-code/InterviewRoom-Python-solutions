# PROBLEM: Sort an array of 0s, 1s and 2s
# https://leetcode.com/problems/sort-colors/
# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0


from typing import List

# SOLUTION
def sort_array(nums: List[int]):
    l=0
    m=0
    h=len(nums)-1

    while m<=h:
        if nums[m]==0:
            nums[m], nums[l] = nums[l], nums[m]
            m+=1
            l+=1
        elif nums[m]==1:
            m+=1
        else:
            nums[m], nums[h] = nums[h], nums[m]
            h-=1
    
    print(nums)


if __name__ == "__main__":
    # INPUT :
    nums = [2,0,2,1,1,0]

    # OUTPUT :
    sort_array(nums)