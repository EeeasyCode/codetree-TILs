num_arr = []
for _ in range(4):
    num_arr.append(list(map(int, input().split())))

total_num = 0
for i in range(4):
    total_num += sum(num_arr[i][:i+1])

print(total_num)
