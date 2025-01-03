score_arr = []
total_score = 0
for _ in range(2):
    score_arr.append(list(map(int, input().split())))

for i in range(2):
    row_avg = sum(score_arr[i]) / 4
    total_score += sum(score_arr[i])
    print(row_avg, end=' ')

print()

for i in range(4):
    col_avg = (score_arr[0][i] + score_arr[1][i]) / 2
    print(col_avg, end=' ')

print()

print(round(total_score/8, 1))
