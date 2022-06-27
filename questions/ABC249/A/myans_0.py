A, B, C, D, E, F, X = map(int, input().split())

ta_q, ta_mod = divmod(X, A + C)
ao_q, ao_mod = divmod(X, D + F)

#print(ta_q, ta_mod)
ta_ful = A * B
ta_len = ta_q * ta_ful
if ta_mod <= A:
    ta_len += ta_mod * B
else:
    ta_len += ta_ful

ao_ful = D * E
ao_len = ao_q * ao_ful
if ao_mod <= D:
    ao_len += ao_mod * E
else:
    ao_len += ao_ful

#print("ta_len:", ta_len)
#print("ao_len:", ao_len)
if ta_len > ao_len:
    print("Takahashi")
elif ta_len == ao_len:
    print("Draw")
else:
    print("Aoki")
