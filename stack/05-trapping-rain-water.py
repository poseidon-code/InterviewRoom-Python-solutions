# PROBLEM: Trapping rain water
# https://leetcode.com/problems/trapping-rain-water/
# https://www.interviewbit.com/problems/rain-water-trapped/


from typing import List


# SOLUTION
def trap (height: List[int]) -> int:
    h1, h2 = 0, 0
    total = 0

    l=0
    r=len(height)-1
    while l<r:
        if height[l]<height[r]:
            h1 = max(h1, height[l])
            total += h1 - height[l]
            l+=1
        else:
            h2 = max(h2, height[r])
            total += h2 - height[r]
            r-=1
    
    return total



if __name__ == "__main__":
    # INPUT :
    height = [0,1,0,2,1,0,1,3,2,1,2,1]

    # OUTPUT :
    print(trap(height))