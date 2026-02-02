n = int(input())
x = list(map(int, input().split()))

moves = 0
for i in range(1, n):
    if x[i] < x[i - 1]:
        moves += x[i - 1] - x[i]
        x[i] = x[i - 1]

print(moves)