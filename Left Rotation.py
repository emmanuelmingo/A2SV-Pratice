import math
import os
import random
import re
import sys
def rotateLeft(d, arr):
    k = len(arr)
    new_arr = [0]*k
    for i in range(k):
        new_arr[(i-d)% k] = arr[i]
    return new_arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
