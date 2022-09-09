from collections import deque, defaultdict

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

N = nextInt()
S = list(str(input()))

ans = 0
q = deque()
count_d = defaultdict(int)

for c in S:
    q.append(c)  ## dequeの"右端"に要素を一つ追加する。
    count_d[c] += 1
    p *= c

    while q and p > k: ## 要素の積がKを超えているか？
        rm = q.popleft() ## 条件を満たさないのでdequeの"左端"から要素を取り除く
        p //= rm ## 取り除いた値に応じて要素の積を更新する

    ans = max(ans, len(q)) ## dequeに入っている要素の積がK以下になるまで区間を縮めた。

print(ans)