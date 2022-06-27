import queue

def solve():
    n = int(input())
    a, b, c = map(int, input().split())
    
    q = queue.Queue()
    q.put((0, 0)) # a, b, cの1つ前の合計、1つ前の枚数の合計
    while not q.empty():
        tmp = q.get()
        print(tmp)
        if tmp[0] == n:
            print(tmp[1])
            return
        else:
            q.put((tmp[0] + a, tmp[1] + 1))
            q.put((tmp[0] + b, tmp[1] + 1))
            q.put((tmp[0] + c, tmp[1] + 1))
         
solve()