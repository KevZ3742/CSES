from itertools import permutations

n = list(input())

toPrint = list(set(permutations(n)))
toPrint.sort()

print(len(toPrint))
for s in toPrint:
    print("".join(s))