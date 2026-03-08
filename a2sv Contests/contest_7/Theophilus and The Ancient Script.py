n = int(input())
output = []
for _ in range(n):
    p = int(input())
    letters = list(input())
    count = 0
    seen = set()
    for i in range(p-1,-1,-1):
        if letters[i] == "A":
          k = i
          while k+1 < p and (letters[k+1] == "B" and k not in seen):
             letters[k], letters[k+1] = letters[k+1],letters[k]
             seen.add(k)
             k += 1
             count += 1
    output.append(count)
for out in output:
    print(out)