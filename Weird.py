if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 0 and (n > 20 or n < 6):
        print("Not Weird")
    else:
        print("Weird")