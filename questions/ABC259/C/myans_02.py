import queue

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

# do bfs until it is over the length of T
# no the other way make it shorter

def main():
    s = str(input())
    t = str(input())
    if s[0:2] != t[0:2]:
        print("No")
        return
    for i in range(2, len(t)):
        #print("s,t: ", s,t)
        if len(s) <= i or s[i] != t[i]:
            # print("i", i)
            if s[i-1] != s[i-2]:
                print("No")
                return                
            else:
                if t[i] == s[i-1]:
                    s = s[:i] + s[i-1] + s[i:]
                else:
                    print("No")
                    return
    if s == t:
        print("Yes")
    else:
        print("No")
    return
    
if __name__ == "__main__":
    main()