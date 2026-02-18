if __name__ == "__main__":
    n = int(input())
    output = []
    for _ in range(n):
        word = input()
        if len(word) < 11:
            output.append(word)
        else:
            k = len(word)-2
            output.append(word[0] + str(k) + word[-1])
    for out in output:
        print(out)