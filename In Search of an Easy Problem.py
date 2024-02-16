#Link :    https://codeforces.com/problemset/problem/1030/A
#   # Time complexity: O(n)


def In_Search_of_an_Easy_Problem(arr):
    if 1 in arr:
        return "HARD"
    else:
        return "EASY"   
n = int(input())
arr = list(map(int, input().split()))
print(In_Search_of_an_Easy_Problem(arr))
