# ou are given two positive integers a
#  and b
# . In one move you can increase a
#  by 1
#  (replace a
#  with a+1
# ). Your task is to find the minimum number of moves you need to do in order to make a
#  divisible by b
# . It is possible, that you have to make 0
#  moves, as a
#  is already divisible by b
# . You have to answer t
#  independent test cases.

# Input
# The first line of the input contains one integer t
#  (1≤t≤104
# ) — the number of test cases. Then t
#  test cases follow.

# The only line of the test case contains two integers a
#  and b
#  (1≤a,b≤109
# ).

# Output
# For each test case print the answer — the minimum number of moves you need to do in order to make a
#  divisible by b
# .

# Example
# inputCopy
# 5
# 10 4
# 13 9
# 100 13
# 123 456
# 92 46
# outputCopy
# 2
# 5
# 4
# 333
# 0


# Solution:
# 1. Take input from the user
# 2. Split the input into a list
# 3. Convert the list into integers
# 4. If a is divisible by b, print 0
# 5. If a is not divisible by b, find the remainder and print b - remainder
# 6. Repeat for all test cases

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    if a%b == 0:
        print(0)
    else:
        print(b - a%b)
    
# This code takes O(1) time complexity to execute.
        