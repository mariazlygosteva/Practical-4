scores = input().split()
highest_score = int(scores[0])

for max in scores:
    if int(max) > highest_score:
        highest_score = int(max)
print(highest_score)