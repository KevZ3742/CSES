n = str(input())

maxRep = 0
currRep = 1
prev = -1
for char in n:
    if char == prev:
        currRep += 1
    else:
        currRep = 1
        prev = char

    maxRep = max(maxRep, currRep)

print(maxRep)