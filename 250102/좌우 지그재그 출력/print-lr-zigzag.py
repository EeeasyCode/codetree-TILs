n = int(input())
current_num = 1
for i in range(n):
    if i % 2 == 0:
        for j in range(current_num, current_num+n):
            print(j, end=' ')
        print()
        current_num += n
    else:
        for j in range(current_num+n-1, current_num-1, -1):
            print(j, end=' ')
        print()
        current_num += n
