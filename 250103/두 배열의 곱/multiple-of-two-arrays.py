one_arr = []
two_arr = []

for _ in range(3):
    one_arr.append(list(map(int, input().split())))

input()

for _ in range(3):
    two_arr.append(list(map(int, input().split())))

for row in range(3):
    for col in range(3):
        print(one_arr[row][col] * two_arr[row][col], end=' ')
    print()