N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

#print(N)
#print(P)
#print(Q)

len_list = []

for start_p_place, start_p in enumerate(P):
    #print("start_p_place", start_p_place)
    len_sequence = 0
    start_q_place = 0
    for i, p in enumerate(P[start_p_place:]):
        #print("search_p", p)
        #print("start_q_place", start_q_place)
        for j, q in enumerate(Q[start_q_place: ]):
            if q % p == 0:
                #print("p, q", p, q)
                start_q_place = start_q_place + j + 1
                #print("next start_q_place", start_q_place)
                len_sequence+=1#
                break
    #print("last len_sequence", len_sequence)
    len_list.append(len_sequence)

#print(len_list)
print(max(set(len_list)))