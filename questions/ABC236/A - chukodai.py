S = str(input())
a, b = map(int, input().split())

a -= 1
b -= 1
#print("S, a, b: ", S, a, b)
s_list = list(S)
s_list[a], s_list[b] = s_list[b], s_list[a]
print("".join(s_list))
