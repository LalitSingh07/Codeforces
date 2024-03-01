
string = input().strip()
if string == '{}':
    print(0)
else:
    distinct_letters = {letter for letter in string[1:-1].split(', ')}
    print(len(distinct_letters))