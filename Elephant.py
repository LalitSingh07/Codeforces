##https://codeforces.com/problemset/problem/617/A

def elephant(x):
    if x%5==0:
        return x//5
    else:
        return x//5+1
    
print(elephant(int(input())))
