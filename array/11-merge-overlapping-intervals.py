# PROBLEM: Merge overlapping intervals
# https://leetcode.com/problems/merge-intervals/
# https://www.interviewbit.com/problems/merge-intervals/


from typing import List


# SOLUTION
def merge_intervals (intervals: List[List[int]]) -> List[List[int]] :
    if len(intervals)<=1:
        return intervals

    intervals.sort(key=lambda a: a[0])
    
    result = []
    result.append(intervals[0])

    for i in range(1, len(intervals)):
        if result[-1][1] < intervals[i][0]:
            result.append(intervals[i])
        else:
            result[-1][1] = max(result[-1][1], intervals[i][1])
        
    return result


if __name__ == "__main__":
    # INPUT :
    intervals = [[1,3],[2,6],[8,10],[15,18]]

    # OUTPUT :
    print(merge_intervals(intervals))