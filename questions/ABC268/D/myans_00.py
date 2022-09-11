import itertools

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

def solve():
    N, M = nextInts()
    S = []
    for _ in range(N):
        S.add(str(input()))
    T = set()
    for _ in range(M):
        T.add(str(input()))

    cand_set = set()
    for v in list(itertools.permutations(S)):
        v_len = len(v)
        v_new = []
        len_one_sp = 0
        for i, p in enumerate(v):
            if not i == (v_len - 1):
                p += "_"
            v_new.append(p)
            len_one_sp += len(p)
        print(v_new)
        rem = 16 - len_one_sp
        
  
    print(cand_set - T)

solve()