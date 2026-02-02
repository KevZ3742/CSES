t = int(input())

for _ in range(t):
    y, x = map(int, input().split())

    inputMax = max(y, x)
    inputMin = min(y, x)
    if inputMax % 2 == 0:
        if y == inputMax:
            print(inputMax ** 2 - inputMin + 1)
        else:
            print((inputMax - 1) ** 2 + inputMin)
    else:
        if x == inputMax:
            print(inputMax ** 2 - inputMin + 1)
        else:
            print((inputMax - 1) ** 2 + inputMin)