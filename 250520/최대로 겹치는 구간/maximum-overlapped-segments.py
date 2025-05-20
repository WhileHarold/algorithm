OFFSET = 100

n = int(input())
segments = [
    map(int, input().split())
    for _ in range(n)
]

blocks = [0] * 201

for a, b in segments:
    a, b = a + OFFSET, b + OFFSET
    
    for i in range(a, b):
        blocks[i] += 1

max_line = max(blocks)
print(max_line)