import math

k = int(input())    

for i in range(1, k + 1):
    total = math.comb(i * i, 2)
    overlap = 4 * (i - 2) * (i - 1)

    print(total - overlap)