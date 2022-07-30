from operator import imod
from queue import Queue

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

def solve():
    ans = 0
    n, m = nextInts()
    x_list = nextIntList()
    m_list = [0 for _ in range(5000)]
    for i in range(m):
        c, y = nextInts()
        m_list[c] = y

    q = Queue()
    q.put({
        "len": 0,
        "c": 1,
        "ans": x_list[0] + m_list[0]
    })
    while not q.empty():
        tmp = q.get()
        print("tmp: ", tmp)
        if tmp["len"] < n:
            if tmp["c"] != 0:
                q.put({
                    "len": tmp["len"] + 1,
                    "c": 0,
                    "ans": tmp["ans"],
                })
            q.put({
                "len": tmp["len"] + 1,
                "c": tmp["c"] + 1,
                "ans": tmp["ans"] + x_list[tmp["len"]] + m_list[tmp["c"]],
            })
        elif tmp["len"] == n:
            ans = max(ans, tmp["ans"])
    print(ans)
    
solve()