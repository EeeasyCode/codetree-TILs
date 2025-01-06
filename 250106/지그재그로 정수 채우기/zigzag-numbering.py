n, m = map(int, input().split())

# Write your code here!
num_arr = [[0] * m for _ in range(n)]
cnt = 0

for i in range(m):
    if i % 2 == 0:
        for j in range(n):
            num_arr[j][i] = cnt
    else:
        for j in range(n-1, 0, -1):
            num_arr[j][i] = cnt

print(num_arr)

    
        
