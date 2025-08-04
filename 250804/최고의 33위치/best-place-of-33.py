n = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

max_coin = 0

for i in range(n- 2):
    for j in range(n - 2):
        coin_count = 0
        for dx in range(3):
            for dy in range(3):
                coin_count += grid[i + dx][j + dy]
        max_coin = max(max_coin, coin_count)

print(max_coin)
