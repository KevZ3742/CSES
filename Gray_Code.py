n = int(input())

dp = [[]] * n
dp[0] = ["0", "1"]

for i in range(1, n):
    dp[i] = ["0" +  code for code in dp[i - 1]]

    temp = dp[i - 1][::-1]
    for code in temp:
        dp[i].append("1" + code)

for code in dp[-1]:
    print(code)