n = int(input())

# Write your code here!
def sum_num(n):
    cnt = 0
    for i in range(1, n+1):
        cnt += i
    cnt //= 10
    return cnt

print(sum_num(n))