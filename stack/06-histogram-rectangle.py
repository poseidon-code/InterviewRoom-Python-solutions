# PROBLEM: Largest rectangle in a histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/
# https://www.interviewbit.com/problems/largest-rectangle-in-histogram/


from typing import List

# SOLUTION
def rectangle (heights: List[int]) -> int:
    stack = []
    l = len(heights)
    max_area = 0

    i=0
    while i<=l:
        h = 0 if i==l else heights[i]

        if len(stack)==0 or h>=heights[stack[-1]]:
            stack.append(i)
        else:
            tp = stack[-1]
            stack.pop()
            max_area = max(max_area, heights[tp]*(i if len(stack)==0 else i-1-stack[-1]))
            i-=1
        i+=1

    return max_area


if __name__ == "__main__":
    # INPUT :
    heights = [2,1,5,6,2,3]

    # OUTPUT :
    print(rectangle(heights))