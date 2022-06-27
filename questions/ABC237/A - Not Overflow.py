N = int(input())

if (N >= pow(-2, 31)) and (N < pow(2, 31)):
    print("Yes")

else:
    print("No")