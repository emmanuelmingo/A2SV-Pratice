def count_less_elements(n, m, a, b):
    i = 0
    result = []

    for j in range(m):
        while i < n and a[i] < b[j]:
            i += 1
        result.append(i)

    return result


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = count_less_elements(n, m, a, b)
print(*result)