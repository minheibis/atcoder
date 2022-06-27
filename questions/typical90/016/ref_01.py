import sys


def euclidean_algo(x, y):
    if not y: return x, 1, 0
    num, new_y, new_x = euclidean_algo(y, x%y)
    new_y -= x//y*new_x
    return num, new_x, new_y

def main(inp):
    N = int(inp())
    A, B, C = reversed(sorted(map(int, inp().split())))
    limit = answer = int(1e5)
    num, x, y = euclidean_algo(B, C)
    for i in range(limit):
        count = N - A * i
        if(count >= 0) and (count%num == 0):
            j = x * (count//num)
            k = y * (count//num)
            k_buf = k % (B//num)
            j -= (k_buf-k) // (B//num) * (C//num)
            k = k_buf
            if j >= 0:
                answer = min(answer, i+j+k)
 
    print(answer)


main(sys.stdin.readline)