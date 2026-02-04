n = int(input())

total = n * (n+1) // 2

if total % 2 == 1:
    print("NO")
    exit()

setSum = total // 2
arr = list(range(n, 0, -1))
arr1 = []
arr2 = []
for i in range(n):
    if setSum - arr[i] >= 0:
        setSum -= arr[i]
        arr1.append(arr[i])
    else:
        arr2.append(arr[i])
    i += 1

print("YES")
print(len(arr1))
print(*arr1)
print(len(arr2))
print(*arr2)