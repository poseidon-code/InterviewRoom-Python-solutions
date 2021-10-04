# PROBLEM: First non-repeating character in a stream
# https://practice.geeksforgeeks.org/problems/first-non-repeating-character-in-a-stream1216/1


# SOLUTION
def non_repeating(a: str) -> str:
    count = [0]*26
    q = []
    result = ""

    for x in a:
        q.append(x)
        count[ord(x)-ord('a')]+=1

        if (len(q)!=0 and count[ord(q[0])-ord('a')]==1):
            result += q[0]
        elif (count[ord(q[0])-ord('a')]>1):
            while (len(q)!=0 and count[ord(q[0])-ord('a')]>1):
                q = q[1:]
            
            if len(q)!=0: result += q[0]
            else: result += '#'
    
    return result



if __name__ == "__main__":
    # INPUT :
    a = "aabc"

    # OUTPUT :
    print(non_repeating(a))