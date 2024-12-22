# -*- coding: utf-8 -*-
"""HackerRank-ImageSeg1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FctIhwIxhU-MirjCimliZjlUJf1F9eDe
"""

from scipy.stats import pearsonr

physics_scores = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history_scores = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

r = pearsonr(physics_scores, history_scores)

print(f"{r[0]:.3f}")