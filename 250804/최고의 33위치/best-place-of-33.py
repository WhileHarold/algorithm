n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

max_coin = 0

for i in range(n - 2):
    for j in range(n - 2):
        count_coin = 0
        for dx in range(3):
            for dy in range(3):
                count_coin += grid[i + dx][i + dy]
                max_coin = max(count_coin, max_coin)

print(max_coin)
