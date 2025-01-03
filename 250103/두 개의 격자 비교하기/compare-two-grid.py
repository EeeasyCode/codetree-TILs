n, m = map(int, input().split())

one_arr = []
two_arr = []
new_arr = [[1] * m for _ in range(n)]
for _ in range(n):
    one_arr.append(list(map(int, input().split())))

for _ in range(n):
    two_arr.append(list(map(int, input().split())))

for row in range(n):
    for col in range(m):
        if one_arr[row][col] == two_arr[row][col]:
            new_arr[row][col] = 0

for row in range(n):
    for col in range(m):
        print(new_arr[row][col], end=' ')
    print()