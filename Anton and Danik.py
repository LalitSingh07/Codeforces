
# https://codeforces.com/problemset/problem/734/A

n = int(input())
game = input()
a = game.count('A')
d = game.count('D')

if a > d:
    print('Anton')
elif a==d:
    print('Friendship')
else:
    print('Danik')
