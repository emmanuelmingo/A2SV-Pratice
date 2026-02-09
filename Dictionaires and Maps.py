import sys
if __name__ == "__main__":
    n = int(input())
    hashmap = {}
    output = []
    for i in range(n):
        k = input().split()
        hashmap[k[0]] = k[1]
    for line in sys.stdin:
        query = line.strip()
        if query in hashmap:
            output.append(query +"="+str(hashmap[query]))
        else:
            output.append("Not found")
    for out in output:
        print(out)