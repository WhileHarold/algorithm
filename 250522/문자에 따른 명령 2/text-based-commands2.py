dirs = list(input())
n = len(dirs)

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

x, y = 0, 0
dir_num = 3

for s in dirs:

    if s == "F":
        x, y = x + dx[dir_num], y + dy[dir_num]
    
    elif s == "L":
        dir_num = (dir_num -1 + 4) % 4

    elif s == "R":
        dir_num = (dir_num + 1) % 4

print(x, y)