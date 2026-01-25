if __name__ == "__main__":
    arr = input().split()
    n = int(arr[0])
    k = int(arr[1])
    output = [0]*(n)
    for i in range(round(n/2)):
        if i == 0:
            output[i] = 1
        else:
            output[i] = output[i-1] + 2
    for i in range(round(n/2),n):
        if i == round(n/2):
            output[i] = 2
        else:
            output[i] = output[i-1] + 2
    print(output[k-1])