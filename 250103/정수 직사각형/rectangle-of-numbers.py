n, m = map(int, input().split())
num_arr = [[0] * m for _ in range(n)]

num = 1
for row in range(n):
    for col in range(m):
        num_arr[row][col] = num
        num += 1

for row in range(n):
    for col in range(m):
        print(num_arr[row][col], end=' ')
    print()
