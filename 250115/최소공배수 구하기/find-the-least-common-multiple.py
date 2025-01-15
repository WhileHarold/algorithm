n, m = map(int, input().split())

# Write your code here!
def lcm(n, m):
    for i in range(1, min(n,m)+1):
        if n % i == 0 and m % i == 0:
            gcd = i
    a = n // gcd
    b = m // gcd

    print(a * b * gcd)


lcm(n, m)
    

