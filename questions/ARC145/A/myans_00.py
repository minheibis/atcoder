from queue import Queue

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())
 
def solve():
    n = nextInt()
    s = str(input())
    len_s = len(s)

    fin_set = set(s)
    q = Queue()
    q.put(s)

    while q.empty() is False:
        s_tmp = q.get()
        print("s_tmp:", s_tmp)
        if s_tmp == s_tmp[::-1]:
            print("Yes")
            return
        for i in range(len_s - 1):
            s_swap = list(s_tmp)
            s_swap[i], s_swap[i + 1] = "A", "B"
            s_swap = str(s_swap)
            print("s_swap:", s_swap)
            if s_swap not in fin_set:
                q.put(s_swap)
    
    print("No")
    return

solve()