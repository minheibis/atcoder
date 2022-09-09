def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

day_dict = {
    "Monday": 5,
    "Tuesday": 4,
    "Wednesday": 3,
    "Thursday": 2,
    "Friday": 1,
}

def solve():
    S = str(input())
    print(day_dict[S])

solve()