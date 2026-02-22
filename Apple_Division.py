n = int(input())
p = list(map(int, input().split()))

toPrint = totalWeight = sum(p)

def dfs(i, prefixSum):
    global toPrint

    if i == n:
        toPrint = min(toPrint, abs(totalWeight - 2 * prefixSum))
        return
    
    dfs(i+1, prefixSum + p[i])
    dfs(i+1, prefixSum)

dfs(0,0)

print(toPrint)