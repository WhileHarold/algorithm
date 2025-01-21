a, b = map(int, input().split())

def magic_number(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    cnt = 0
    while n > 0:
        cnt += n % 10
        n //= 10

    if cnt % 2 != 0:
        return False

    return True


cnt = 0
for i in range(a, b + 1):
    if magic_number(i):
        cnt += 1

print(cnt)
