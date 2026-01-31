n = int(input())
numbers = set(map(int, input().split()))

found = False
for i in range(1, n):
    if i not in numbers:
        found = True
        print(i)
        break

if found == False:
    print(n)