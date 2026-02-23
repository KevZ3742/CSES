board = []
for _ in range(8):
    board.append(input())

toPrint = 0

def backtrack(row, cols, diag1, diag2):
    global toPrint

    if row == 8:
        toPrint += 1
        return
    
    for c in range(8):
        if board[row][c] == "." and not cols[c] and not diag1[row + c] and not diag2[row + 7 - c]:
            cols[c] = True
            diag1[row + c] = True
            diag2[row + 7 - c] = True
            backtrack(row + 1, cols, diag1, diag2)
            cols[c] = False
            diag1[row + c] = False
            diag2[row + 7 - c] = False
            

cols = [False] * 8
diag1 = [False] * 15
diag2 = [False] * 15

backtrack(0, cols, diag1, diag2)

print(toPrint)