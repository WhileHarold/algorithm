n = int(input())

# Please write your code here.
def get_sum(n):
    if n < 10:
        return n * n
    
    return get_sum(n // 10) + (n % 10) * (n % 10)


print(get_sum(n))