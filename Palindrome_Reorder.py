from collections import Counter

n = input()
counter = Counter(n)

toPrint = []

centerLetter = ""
center = len(n) % 2
for key in counter:
    if counter[key] % 2 != 0:
        if counter[key] // 2 > 0:
            toPrint.append(key * (counter[key] // 2))
        centerLetter = key
        center -= 1
    else:
        toPrint.append(key * (counter[key] // 2))

    if center < 0:
        print("NO SOLUTION")
        exit()

print("".join(toPrint) + centerLetter + "".join(toPrint[::-1]))