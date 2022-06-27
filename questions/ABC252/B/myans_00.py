n, k = map(int, input().split())
a = [-1] + list(map(int, input().split()))
b = set(map(int, input().split()))

def func():
    x = max(a)
    for i, a_num in enumerate(a):
        if a_num == x:
            if i in b:
                print("Yes")
                return
    print("No")
    return

func()
