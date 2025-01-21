a, o, c = input().split()
a = int(a)
c = int(c)

# Write your code here!
def operations(a, o, c):
    if o == '+':
        print(f"{a} + {c} = {a+c}")
    elif o == '-':
        print(f"{a} - {c} = {a-c}")
    elif o == '/':
        print(f"{a} / {c} = {a//c}")
    elif o == '*':
        print(f"{a} * {c} = {a*c}")
    else:
        print("False")


operations(a, o, c)

