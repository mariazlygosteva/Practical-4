score = input().split(':')
team1 = int(score[0])
team2 = int(score[1])
if team1 > team2:
    print(1)
elif team2 > team1:
    print(2)
else:
    print(0)