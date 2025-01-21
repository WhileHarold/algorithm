a, b = map(int, input().split())

# Write your code here!
def onjeonsu(a, b):
    cnt = 0
    for i in range(a, b+1):
        if i % 2 == 0 or i % 5 == 0 or (i % 3 == 0 and i % 9 != 0):
            cnt += 1
    print((b-a+1)-cnt)


onjeonsu(a,b)