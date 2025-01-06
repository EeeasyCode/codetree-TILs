n = int(input())

num_arr = [[0] * n for _ in range(n)]
cnt = 1

for i in range(n):
    for j in range(n):
        num_arr[j][i] = cnt
        cnt += 1

for nums in num_arr:
    for num in nums:
        print(num, end=' ')
    print()