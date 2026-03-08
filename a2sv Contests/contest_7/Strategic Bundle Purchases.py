n = int(input())
output = []
for _ in range(n):
    items, coupons = map(int, input().split())
    prices = sorted(list(map(int, input().split())))
    discount = sorted(list(map(int, input().split())))
    price = 0
    start = 0
    for dis in discount:
        if prices:
           if dis == 1:
              prices.pop()
              items -= 1
              continue
           if dis > len(prices):
               break
           start = items - dis + 1
           if len(prices[start-1:]) != 1:
              price += sum(prices[start:])
           prices = prices[:start-1]
        else:
            break
    if prices:
        for p in prices:
            price += p
    output.append(price)
for out in output:
    print(out)
