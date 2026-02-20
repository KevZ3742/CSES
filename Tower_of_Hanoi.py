n = int(input())

moves = []

def hanoi(n, start, stop, temp):
    if n == 0:
        return
    
    hanoi(n - 1, start, temp, stop)
    moves.append((start, stop))
    hanoi(n - 1, temp, stop, start)

hanoi(n, 1, 3, 2)

print(len(moves))
for move in moves:
    print(*move)