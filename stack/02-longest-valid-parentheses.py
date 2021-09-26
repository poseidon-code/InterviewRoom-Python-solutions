# PROBLEM: Length of longest valid parentheses
# https://leetcode.com/problems/longest-valid-parentheses/


# SOLUTION
def longest_length (s: str) -> int:
    parentheses = []
    parentheses.append(-1)
    result = 0

    for i in range(len(s)):
        if s[i]=='(':
            parentheses.append(i)
        else:
            parentheses.pop()

            if (len(parentheses)==0):
                parentheses.append(i)
            else:
                result = max(result, i - parentheses[-1])
    
    return result


if __name__ == "__main__":
    # INPUT :
    s = ")()())"

    # OUTPUT :
    print(longest_length(s))