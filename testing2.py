import math

import numpy as np

a = 7
b = -7

c = abs(a - b)
print(c)


"""plotting the regression
max_x = np.max(pair_function[:, 0])
min_x = np.min(pair_function[:, 0])

# calculating the regression line values
x = np.linspace(min_x, max_x, 500)
y = intercept_f + slope_f * x

# plotting line
plt.plot(x, y, label='Regression')

# plotting scatter points
plt.scatter(pair_function[:, 0], pair_function[:, 1], label='function')
plt.show()"""