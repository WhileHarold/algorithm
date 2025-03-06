n = int(input())

# Please write your code here.
def get_sum(n):
    if n == 0:
        return 0
    
    return get_sum(n-1) + n


print(get_sum(n))