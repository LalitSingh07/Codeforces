# Link 

# Time complexity: O(n)
# Space complexity: O(n)




def Queue_at_the_School(n, t, s):
    for _ in range(t):
        s = s.replace('BG', 'GB')
    return s
 # GBGGB

student , time = map(int, input().split())
str = input()

print(Queue_at_the_School(student, time, str))