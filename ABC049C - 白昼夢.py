S = str(input())
S = S[::-1]

word_list = ["dream", "dreamer", "erase", "eraser"]
word_list = [word[::-1] for word in word_list]

cnt = 0
for i in range(len(S)):
    if i == cnt:
        for j in range(4):
            if S[i:i+len(word_list[j])] == word_list[j]:
                cnt += len(word_list[j])
                break

if cnt == len(S):
    print("YES")
else:
    print("NO")