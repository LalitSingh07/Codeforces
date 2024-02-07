player_num ,place = map(int,input().split())
player_score=list(map(int,input().split()))
count = 0
for i in range(player_num):
    if player_score[i]>=player_score[place-1] and player_score[i]>0:
        count+=1
print(count)