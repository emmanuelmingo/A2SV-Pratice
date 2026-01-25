if __name__  == "__main__":
    n = int(input())
    output = []
    for i in range(n):
        exp = str(input())
        output.append(int(exp[0])+ int(exp[2]))
    for out in output:
        print(out)