n, m = map(int, input().split())

arr1 = []
arr2 = []

pos1 = 0
pos2 = 0

for _ in range(n):
    d, t = input().split()
    t = int(t)
    for _ in range(t):
        pos1 = pos1 - 1 if d == "L" else pos1 + 1
        arr1.append(pos1)

for _ in range(m):
    d, t = input().split()
    t = int(t)
    for _ in range(t):
        pos2 = pos2 - 1 if d == "L" else pos2 + 1
        arr2.append(pos2)

max_len = max(len(arr1), len(arr2))

if len(arr1) < max_len:
    arr1 += [arr1[-1]] * (max_len - len(arr1))
if len(arr2) < max_len:
    arr2 += [arr2[-1]] * (max_len - len(arr2))

for i in range(max_len):
    if arr1[i] == arr2[i]:
        print(i + 1)  
        break
else:
    print(-1)
