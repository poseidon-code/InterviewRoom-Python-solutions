# PROBLEM: Edit distance
# https://leetcode.com/problems/edit-distance/


# SOLUTION
def edit_distance (word1: str, word2: str) -> int:
    m, n, pre = len(word1), len(word2), 0
    result = [0]*(n+1)
    for i in range(1, n+1) : result[i] = i
    
    for i in range(1, m+1):
        pre = result[0]
        result[0] = i

        for j in range(1, n+1):
            temp = result[j]
            if word1[i-1]==word2[j-1]:
                result[j] = pre
            else:
                result[j] = min(pre, min(result[j-1], result[j])) + 1
            pre = temp

    return result[n]



if __name__ == "__main__":
    # INPUT :
    word1 = "horse"
    word2 = "ros"

    # OUTPUT :
    print(edit_distance(word1, word2))