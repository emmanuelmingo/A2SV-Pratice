if __name__ == "__main__":
    totalPrice = 0
    output = 0
    arr = input().split()
    unitPrice, balance, amount = int(arr[0]),int(arr[1]),int(arr[2])
    for i in range(1,amount+1):
        totalPrice += unitPrice*i
    if balance > totalPrice:
        print(output)
    else:
        output = totalPrice - balance
        print(output)