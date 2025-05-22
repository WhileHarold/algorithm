dx = {'E': 1, 'W': -1, 'S': 0, 'N': 0}
dy = {'E': 0, 'W': 0, 'S': -1, 'N': 1}

N = int(input()) 
x, y = 0, 0       

for _ in range(N):
    dir, dis = input().split()
    dis = int(dis)
    x += dx[dir] * dis
    y += dy[dir] * dis

print(x, y)
