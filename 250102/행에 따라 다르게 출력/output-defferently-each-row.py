n = int(input())
current_num = 0

for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            current_num += 1
            print(current_num, end=" ")
        print()
    else:
        for j in range(n):
            current_num += 2
            print(current_num, end=" ")
        print()
    
