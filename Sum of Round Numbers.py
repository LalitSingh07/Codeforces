

n = int(input())
for i in range(n):
    num = input()
    num = num[::-1]
    ans = []
    for j in range(len(num)):
        if num[j] != '0':
            ans.append(str(num[j] + '0' * j))
    print(len(ans))
    print(' '.join(ans))
