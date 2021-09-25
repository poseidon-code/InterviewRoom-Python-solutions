# PROBLEM: Valid parenthesis
# https://leetcode.com/problems/valid-parentheses/


# SOLUTION
def is_valid (s: str) -> bool:
    parenthesis = []

    for c in s:
        if c=='{':
            parenthesis.append('}')
        elif c=='[':
            parenthesis.append(']')
        elif c=='(':
            parenthesis.append(')')
        else:
            if len(parenthesis)==0 or c!=parenthesis.pop():
                return False
    
    return len(parenthesis)==0


if __name__ == "__main__":
    # INPUT :
    s = "()[]{}"

    # OUTPUT :
    print(is_valid(s))