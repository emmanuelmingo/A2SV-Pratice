if __name__ == "__main__":
    n = int(input())
    output = []
    for _ in range(n):
        arr = list(map(int, input().split()))
        found = False
        for i in range(len(arr)):
            if arr[i] == arr[i-1] + arr[i-2]:
                found = True
                break
        if found:
            output.append("yes")
        else:
            output.append("no")
    for out in output:
        print(out)