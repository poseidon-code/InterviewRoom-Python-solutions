# PROBLEM: Word Ladder
# https://leetcode.com/problems/word-ladder/
# https://www.interviewbit.com/problems/word-ladder-i/


from typing import List
import collections

# SOLUTION
def ladder_length (begin_word: str, end_word: str, word_list: List[str]) -> int:
    m = len(word_list[0])
    word_list = set(word_list)
    if end_word not in word_list:
        return 0
    word_list.add(begin_word)

    matrix = collections.defaultdict(list)
    for word in word_list:
        for i in range(m):
            s = word[:i] + '_' + word[i+1:]
            matrix[s].append(word)

    queue = [begin_word]
    mark = set()
    mark.add(begin_word)
    dist = 1
    
    while queue:
        next_queue = []
        
        while queue:
            word = queue.pop(0)
            
            for i in range(m):
                s = word[:i] + '_' + word[i+1:]
                
                for next_word in matrix[s]:
                    if next_word not in mark:
                        if next_word == end_word:
                            return dist + 1
                        mark.add(next_word)
                        next_queue.append(next_word)
        
        queue = next_queue
        dist += 1
    
    return 0


if __name__ == "__main__":
    # INPUT :
    begin_word = "hit"
    end_word = "cog"
    word_list = ["hot","dot","dog","lot","log","cog"]

    # OUTPUT :
    print(ladder_length(begin_word, end_word, word_list))