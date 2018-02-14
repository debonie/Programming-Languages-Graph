import numpy as np
import matplotlib.pyplot as plt

#data
groups = 5
ease = (5, 4, 3, 2, 1)
salaries = (5, 1, 3, 2, 4)
companies = (3, 1, 2, 4, 5)

# create the plots
fig, ax = plt.subplots()
index = np.arange(groups)
bar_width = 0.18
opacity = 0.8

rects1 = plt.bar(index, ease, bar_width,
                 alpha = opacity,
                 color = 'b',
                 label = 'Ease to Learn')

rects2 = plt.bar(index + bar_width, salaries, bar_width,
                 alpha = opacity,
                 color = 'g',
                 label = 'Average Salaries')

rects3 = plt.bar(index + (bar_width * 2), companies, bar_width,
                 alpha = opacity,
                 color = 'r',
                 label = 'Most Used by Companies')

plt.xlabel('Programming Languages')
plt.ylabel('Ranks')
plt.title('Programming Languages Ranked (1 lowest to 5 highest)')
plt.xticks(index + bar_width, ('Python', 'Swift', 'Go', 'Java', 'JavaScript'))
plt.legend()

plt.tight_layout()
plt.show()
