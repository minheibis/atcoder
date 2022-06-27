from collections import deque

N, L, W = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
# 最後を追加した方がいいかも。
A = deque(A)
A.append(L)

#print(N, L, W)
#print(A)

end_old = 0
rm_len = 0

while len(A) > 0:
    # 当該クエリ
    a = A.popleft()
    #print(a)
    start = a
    end = a + W
    # その前の区間に被っていなければシートを設置していく。
    if start > end_old:
        rm_len += (((start - 1) - (end_old + 1) + 1) // (W)) + 1
    end_old = end

# 一番右だけ再処理
print(rm_len)
