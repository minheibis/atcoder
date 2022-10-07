def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

s_list = []
for _ in range(10):
    s_list.append(str(input()))

sh_start_flag = False
D = 10
for i, s in enumerate(s_list):
    sh_flag_inline = False
    for j, c in enumerate(s):
        if c == "#" and sh_flag_inline == False:
            sh_flag_inline = True
            C = j + 1
            B = i + 1
            if sh_start_flag == False:
                A = i + 1
                sh_start_flag = True
        elif c == "." and sh_flag_inline == True:
            sh_flag_inline = False
            D = j
print(A, B)
print(C, D)