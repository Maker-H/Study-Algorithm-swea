score = {
    'python': 80,
    'django': 89,
    'web': 83
}

score['algorithm'] = 90
score['python'] = 90

score = score.values()
score_sum = sum(score)

print(score_sum/len(score))
