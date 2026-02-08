t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    if (a + b) % 3 != 0:
        print("NO")
    elif max(a, b) > 2 * min(a, b):
        print("NO")
    else:
        print("YES")