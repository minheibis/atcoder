N = int(input())
S = str(input())

x = 0
y = 0
state_id = 0

for c in S:
    if c == "S":
        if state_id == 0:
            x += 1
        elif state_id == 1:
            y += 1
        elif state_id == 2:
            x -= 1
        elif state_id == 3:
            y -= 1
    elif c == "R":
        state_id -= 1
        state_id %= 4

print(x, y)