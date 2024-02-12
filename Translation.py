word = input()
codes = input()
revword = word[::-1]
if revword == codes:
    print("YES")
else:
    print("NO")
 