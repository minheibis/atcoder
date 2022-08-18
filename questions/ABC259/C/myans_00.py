import queue

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

# do bfs until it is over the length of T

def main():
    s = str(input())
    t = str(input())
    len_t = len(t)
    q = queue.Queue()
    q.put(s)

    while not q.empty():
        now_s = q.get()
        if now_s == t:
            print("Yes")
            return
        # print(now_s)
        for i in range(len(now_s)-1):
            if now_s[i] == now_s[i+1]:
                next_s = now_s[:i+1] + now_s[i] + now_s[i+1:]                  
                if len(next_s) <= len_t:
                    q.put(next_s)
    print("No")
    return
    
if __name__ == "__main__":
    main()