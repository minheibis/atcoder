from collections import Counter

S = str(input())

def B_func(S):
    count_dict = Counter(S)
    # print(count_dict)

    count_lower, count_upper = 0, 0
    for c, num in count_dict.items():
        if num != 1:
            print("No")
            return
        if c.islower():
            count_lower += 1
        else:
            count_upper += 1            
    if count_lower == 0:
        print("No")
        return
    elif count_upper == 0:
        print("No")
        return

    print("Yes")
    return

B_func(S)