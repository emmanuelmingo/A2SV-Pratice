n = int(input())
output = []
for _ in range(n):
    k = int(input())
    players = list(map(int, input().split()))
    if k < 3:
        output.append('NO')
        continue
    players.sort()
    left = 0
    right = k -1
    check = False
    sum_elite = 0
    len_elite = 0
    len_crowd = 0
    sum_crowd = 0
    while left < right:
        sum_elite += players[right]
        right -= 1
        len_elite += 1
        if left < 2:
            sum_crowd += players[left] + players[left+1]
            len_crowd += 2
            left += 2
        else:
            sum_crowd += players[left]
            len_crowd += 1
            left += 1
        if sum_elite > sum_crowd and len_elite < len_crowd:
            output.append('Yes')
            check = True
            break
    if not check:
        output.append('NO')
for out in output:
    print(out)