# PROBLEM: Find square root of a number
# https://leetcode.com/problems/sqrtx/
# https://www.interviewbit.com/problems/square-root-of-integer/


# SOLUTION
def sqrt (x: int) -> int: 
    r = x
    while r*r > x:
        r = (r + x/r)/2
    return int(r)


if __name__ == "__main__":
    # INPUT :
    x = 8

    # OUTPUT :
    print(sqrt(x))