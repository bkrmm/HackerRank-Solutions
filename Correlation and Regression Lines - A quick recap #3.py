"""
PROBLEM STATEMENT:
Here are the test scores of 10 students in physics and history:

Physics Scores  15  12  8   8   7   7   7   6   5   3
History Scores  10  25  17  11  13  17  20  13  9   15
When a student scores 10 in Physics, what is his probable score in History? Compute the answer correct to one decimal place.

Hackerrank Link - https://www.hackerrank.com/challenges/correlation-and-regression-lines-8/
"""

#----------------------------------------------------------------------------------------------------------------------

physics_scores = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history_scores = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

#calculate the mean of scores
mean_physics = sum(physics_scores)/len(physics_scores)
mean_history = sum(history_scores)/len(history_scores)

numerator = sum((x-mean_physics)*(y-mean_history) for x,y in zip(physics_scores, history_scores))
denominator = sum((x-mean_physics)**2 for x in physics_scores)

m = numerator/denominator
b = (mean_history) - (m*(mean_physics))

# y = mx+b
predicted = (m*10) + b
print(f"{predicted:.1f}")
