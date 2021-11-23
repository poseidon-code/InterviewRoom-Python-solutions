# PROBLEM: Median of two sorted arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/
# https://www.interviewbit.com/problems/median-of-array/

from typing import List

# SOLUTION
def median (nums1: List[int], nums2: List[int]) -> float: 
    m, n, l = len(nums1), len(nums2), 0
    r = m
    if m > n : return median(nums2, nums1)

    while l <= r:
        i = int((l+r)/2)
        j = int((m+n+1)/2 - i)

        if i and nums1[i-1]>nums2[j]:
            r = i-1
        elif i<m and nums2[j-1] > nums1[i]:
            l = i+1
        else:
            lmax = nums2[j-1] if not i else nums1[i-1] if not j else max(nums1[i-1], nums2[j-1])
            if (m+n) % 2 : return lmax
            rmin = nums2[j] if i==m else nums1[i] if j==n else min(nums1[i], nums2[j])

            return 0.5 * (lmax + rmin)
    
    return 0.0


if __name__ == "__main__":
    # INPUT :
    nums1 = [1,2]
    nums2 = [3,4]

    # OUTPUT :
    print(median(nums1, nums2))