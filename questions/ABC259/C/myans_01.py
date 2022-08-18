import queue

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

# do bfs until it is over the length of T
# no the other way make it shorter

def main():
    s = str(input())
    t = str(input())
    len_s = len(s)
    q = set()
    q.add(t)

    while len(q) != 0:
        now = q.pop()
        # print(now)
        if now == s:
            print("Yes")
            return
        # print(now_s)
        for i in range(len(now)-1):
            if now[i] == now[i+1]:
                next = now[:i] + now[i+1:]                
                if len(next) >= len_s:
                    q.add(next)
    print("No")
    return
    
if __name__ == "__main__":
    main()