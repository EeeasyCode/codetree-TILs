n = int(input())

num_arr = [[0] * n for _ in range(n)]
cnt = 1

for i in range(n-1, -1, -1):
    if (i % 2 == 0 and n % 2 == 0) or (i % 2 != 0 and n % 2 != 0):
        for j in range(0, n):
            num_arr[j][i] = cnt
            cnt += 1
    else:
        for j in range(n-1, -1, -1):
            num_arr[j][i] = cnt
            cnt += 1

for nums in num_arr:
    for num in nums:
        print(num, end=' ')
    print()

    
