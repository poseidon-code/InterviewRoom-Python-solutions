# PROBLEM: Word Search
# https://leetcode.com/problems/word-search/
# https://www.interviewbit.com/problems/word-search-board/


from typing import List

# SOLUTION
def dfs (board: List[List[str]], i: int, j: int, word: str):
    if len(word) == 0 : return True
    if i<0 or i>=len(board) or j<0 or j>= len(board[0]) or board[i][j]!=word[0] : return False

    c = board[i][j]
    board[i][j] = '*'
    s = word[1:]

    result =   dfs(board, i-1, j, s) \
            or dfs(board, i+1, j, s) \
            or dfs(board, i, j-1, s) \
            or dfs(board, i, j+1, s)
    board[i][j] = c

    return result


def exist (board: List[List[str]], word: str) -> bool:
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board, i, j, word):
                return True
    
    return False


if __name__ == "__main__":
    # INPUT :
    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word = "ABCCED"

    # OUTPUT :
    print(exist(board, word))