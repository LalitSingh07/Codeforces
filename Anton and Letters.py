# # Recently, Anton has found a set. The set consists of small English letters. Anton carefully wrote out all the letters from the set in one line, separated by a comma. He also added an opening curved bracket at the beginning of the line and a closing curved bracket at the end of the line.
 
# # Unfortunately, from time to time Anton would forget writing some letter and write it again. He asks you to count the total number of distinct letters in his set.
 
# # Input
# # The first and the single line contains the set of letters. The length of the line doesn't exceed 1000. It is guaranteed that the line starts from an opening curved bracket and ends with a closing curved bracket. Between them, small English letters are listed, separated by a comma. Each comma is followed by a space.
 
# string = input()
# distinct_letters = {letter for letter in string[1:-1].split(', ')}
# print(len(distinct_letters))
# →Judgement Protocol
# Test: #1, time: 31 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
# Input
# {a, b, c}
# Output
# 3
# Answer
# 3
# Checker Log
# ok 1 number(s): "3"
# Test: #2, time: 46 ms., memory: 0 KB, exit code: 0, checker exit code: 0, verdict: OK
# Input
# {b, a, b, a}
# Output
# 2
# Answer
# 2
# Checker Log
# ok 1 number(s): "2"
# Test: #3, time: 31 ms., memory: 0 KB, exit code: 0, checker exit code: 1, verdict: WRONG_ANSWER
# Input
# {}
# Output
# 1
# Answer
# 0
# Checker Log
# wrong answer 1st numbers differ - expected: '0', found: '1'

string = input().strip()
if string == '{}':
    print(0)
else:
    distinct_letters = {letter for letter in string[1:-1].split(', ')}
    print(len(distinct_letters))