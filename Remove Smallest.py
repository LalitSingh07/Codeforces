n = int(input())
for i in range(n):
    m = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for j in range(1, m):
        if a[j] - a[j-1] > 1:
            print("NO")
            break
    else:
        print("YES")
        