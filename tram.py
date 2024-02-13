## https://codeforces.com/problemset/problem/116/A

#
# Problem: Tram
# Description:


def main():
    n = int(input())
    max_capacity = 0
    current_capacity = 0
    for i in range(n):
        a, b = map(int, input().split())
        current_capacity -= a
        current_capacity += b
        if current_capacity > max_capacity:
            max_capacity = current_capacity
    print(max_capacity)
main()