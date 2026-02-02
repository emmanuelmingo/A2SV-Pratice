def split_and_join(line):
    # write your code here
    splitWord = line.split(" ")
    return "-".join(splitWord)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)