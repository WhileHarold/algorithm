n, m, k = map(int, input().split())
pay = [int(input()) for _ in range(m)]
students = [0] * (n+1)

for i in range(m):
    students[pay[i]] += 1
    if students[pay[i]] == k:
        print(pay[i])
        break

else:
    print(-1)