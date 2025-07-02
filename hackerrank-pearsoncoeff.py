physics = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

n = len(physics)

mean_x = sum(physics) / n
mean_y = sum(history) / n

sum_xy = sum((physics[i] - mean_x) * (history[i] - mean_y) for i in range(n))
sum_xx = sum((physics[i] - mean_x)**2 for i in range(n))
sum_yy = sum((history[i] - mean_y)**2 for i in range(n))

r = sum_xy / (sum_xx*sum_yy)**(1/2)

print(f"{r:.3f}")
