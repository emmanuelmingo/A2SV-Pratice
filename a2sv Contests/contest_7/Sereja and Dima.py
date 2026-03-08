n = int(input())
cards = list(map(int,input().split()))
output = [0]*2
for i in range(n):
    max_val = max(cards[0],cards[-1])
    output[i%2] += max_val
    cards.remove(max_val)
for out in output:
    print(out, end=' ')