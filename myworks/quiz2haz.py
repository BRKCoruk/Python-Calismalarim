def score_summary(scores):
    passed = 0
    total = 0
    for score in scores:
        total = total + score
        if score >= 50:
            passed = passed + 1
    return total, passed

result = score_summary((40,70,90,50))
print(result)