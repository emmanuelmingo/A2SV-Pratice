if __name__ == "__main__":
    n = int(input())
    output = []
    words = []
    for i in range(n):
        words.append(input())
    for word in words:
        if len(word) < 11:
            output.append(word)
        else:
            output.append(word[0]+str(len(word)-2)+word[-1])
    for out in output:
        print(out)