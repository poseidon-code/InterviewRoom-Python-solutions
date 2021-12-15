# PROBLEM: Word Break
# https://leetcode.com/problems/word-break/
# https://www.interviewbit.com/problems/word-break/

from typing import List

# SOLUTION
def word_break (s: str, wordDict: List[str]) -> bool:
    dp = [True]

    for i in range(1, len(s)+1):
        dp += any(dp[j] and s[j:i] in wordDict for j in range(i)),

    return dp[-1]


if __name__ == "__main__":
    # INPUT :
    s = "leetcode"
    wordDict = ["leet", "code"]

    # OUTPUT :
    print(word_break(s, wordDict))