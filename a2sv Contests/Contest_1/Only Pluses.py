if __name__ == "__main__":
    n = int(input())
    output = []
    for i in range(n):
        arr = input().split()
        arrs = []
        for num in arr:
            arrs.append(int(num))
        count = 0
        total = 0
        while count < 5:
            minPosition = arrs.index(min(arrs))
            arrs[minPosition] += 1
            count += 1
        total = arrs[0] * arrs[1] * arrs[2]
        output.append(total)
    for out in output:
        print(out)