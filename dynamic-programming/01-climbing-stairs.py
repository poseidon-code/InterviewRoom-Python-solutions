# PROBLEM: Climbing stairs
# https://leetcode.com/problems/climbing-stairs/

# SOLUTION
def climb_stairs (n: int) -> int: 
    a = b = 1
    for _ in range(n):
        a, b = b, a+b
    return a


if __name__ == "__main__":
    # INPUT :
    n = 3

    # OUTPUT :
    print(climb_stairs(n))