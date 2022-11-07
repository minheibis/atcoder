from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

def nextInt(): return int(input())
def nextInts(): return map(int, input().split())
def nextIntList(): return list(nextInts())

A, B = nextInts()
print(Decimal(str(B/A)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))