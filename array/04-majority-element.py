# PROBLEM: Majority element
# https://leetcode.com/problems/majority-element/
# https://www.interviewbit.com/problems/majority-element/
# https://practice.geeksforgeeks.org/problems/majority-element/0


from typing import List

# SOLUTION
def majority_element (nums: List[int]) -> int:
    major=nums[0]
    count=1

    for n in nums:
        if count == 0:
            count+=1
            major = n
        elif major == n:
            count+=1
        else:
            count-=1

    return major


if __name__ == "__main__":
    # INPUT :
    nums = [3,2,3]

    # OUTPUT :
    print(majority_element(nums))