"""
question link - https://www.hackerrank.com/challenges/correlation-and-regression-lines-7
"""

def get_regr_slope(x,y):
    xy = [a*b for a, b in zip(x,y)]
    n = len(x)
    x_2 = [a*a for a in x]
    num = n*sum(xy) - sum(x)*sum(y)
    denom = n*sum(x_2) - sum(x)**2
    slope = num/denom
    print("%.3f" % slope)

physics = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]


get_regr_slope(physics, history)
