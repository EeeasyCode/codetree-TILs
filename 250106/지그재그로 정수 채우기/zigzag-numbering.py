n, m = map(int, input().split())

# Write your code here!
num_arr = [[0] * m for _ in range(n)]
cnt = 0

for i in range(m):
    if i % 2 == 0:
        for j in range(n):
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

    
        
