# PROBLEM: Power(x,n)
# https://leetcode.com/problems/powx-n/
# https://www.interviewbit.com/problems/implement-power-function/


# SOLUTION
def power (x: float, n: int) -> float: 
    if not n : return 1
    if n<0:
        return 1/power(x, -n)
    if n%2:
        return x*power(x, n-1)

    return power(x*x, n/2)


if __name__ == "__main__":
    # INPUT :
    x = 2.10000
    n = 3

    # OUTPUT :
    print(power(x, n))