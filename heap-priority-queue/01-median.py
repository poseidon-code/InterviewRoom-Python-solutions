# PROBLEM: Find median in a stream
# https://practice.geeksforgeeks.org/problems/find-median-in-a-stream-1587115620/1

from heapq import heappush, heappop

maxq = []
minq = []

def get_median():
    if len(maxq) > len(minq):
        return float(-maxq[0])
    return float(minq[0] - maxq[0])/2

        
def insert_heap(x):
    heappush(maxq, -x)
    heappush(minq, -heappop(maxq))
    if len(minq) > len(maxq):
        heappush(maxq, -heappop(minq))
    

if __name__ == "__main__":
    # INPUT :
    x = [5,15,1,3]

    # OUTPUT :
    for i in x:
        insert_heap(i)
        print(get_median())