# PROBLEM: Generate binary numbers from 1 to n  
# https://www.geeksforgeeks.org/interesting-method-generate-binary-numbers-1-n/


from queue import Queue

# SOLUTION
def generate(n: int):
    q = Queue()
    q.put("1")

    while n > 0:
        n-=1

        s1 = q.get()
        print(s1, end=" ")

        s2 = s1

        q.put(s1+"0")
        q.put(s2+"1")
    
    print()



if __name__ == "__main__":
    # INPUT :
    n = 10

    # OUTPUT :
    generate(n)