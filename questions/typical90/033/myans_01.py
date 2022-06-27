# 1つおきしかなくない？
a, b = map(int, input().split())
if a == 1 or b == 1:
    print(a * b)
else:
    print(((a + 1) // 2) * ((b + 1) // 2))

# いや気づかない笑
