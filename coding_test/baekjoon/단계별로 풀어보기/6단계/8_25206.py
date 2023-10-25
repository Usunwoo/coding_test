arr = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}

cnt = 0
score_sum = 0
for i in range(20):
    _, score, grade = input().split()
    if grade == "P":
        continue
    score = int(score.split(".")[0])
    cnt += score * arr.get(grade)
    score_sum += score

print(cnt/score_sum)
