__author__ = 'caleb'

components = {'sprinkles': (5, -1, 0, 0, 5), 'peanut_butter': (-1, 3, 0, 0, 1), 'frosting': (0, -1, 4, 0, 6),
              'sugar': (-1, 0, 0, 2, 8)}
components2 = {'sprinkles': (-1, -2, 6, 3, 8), 'peanut_butter': (2, 3, -2, -1, 3)}
scores = []
for sprinkle_percent in range(0, 100):
    for pb_percent in range(0, 100 - sprinkle_percent):
        for frosting_percent in range(0, 100 - sprinkle_percent - pb_percent):
            sugar_percent = 100 - sprinkle_percent - pb_percent - frosting_percent
            scoring_metric = [0, 0, 0, 0, 0]
            score = 1
            for i in range(4):
                scoring_metric[i] = sprinkle_percent * components['sprinkles'][i] \
                                    + pb_percent * components['peanut_butter'][i] \
                                    + frosting_percent * components['frosting'][i] \
                                    + sugar_percent * components['sugar'][i]
                if scoring_metric[i] < 0:
                    scoring_metric[i] = 0
                score *= scoring_metric[i]
                calories = sprinkle_percent * components['sprinkles'][4] \
                           + pb_percent * components['peanut_butter'][4] \
                           + frosting_percent * components['frosting'][4] \
                           + sugar_percent * components['sugar'][4]
            if calories == 500:
                scores.append(score)
print max(scores)
