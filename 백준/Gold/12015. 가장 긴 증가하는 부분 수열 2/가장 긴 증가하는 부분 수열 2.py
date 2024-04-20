import sys


def search_right(arr, find):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] == find:
            return mid

        elif arr[mid] > find:
            right = mid
        else:
            left = mid + 1

    return right


input = sys.stdin.readline
N = int(input())
numbers = list(map(int, input().split()))
lis = []

for num in numbers:
    if not lis or lis[-1] < num:
        lis.append(num)
    else:
        index = search_right(lis, num)
        if lis[index] != num:
            lis[index] = num

print(len(lis))
