import numpy as np
import sklearn.metrics as sk

def calc(n_func_train, n_func_ideal):
    # step 1, calculate mean of Y1 and Y2:
    mean_train = np.mean(n_func_train)
    mean_ideal = np.mean(n_func_ideal)

    # step 2, compute the amount of values:
    length = len(n_func_train)

    # step 3, calculate the slope and intercept
    a, b = 0, 0
    for i in range(length):
        a += (n_func_train[i] - mean_train) * (n_func_ideal[i] - mean_ideal)
        b += (n_func_train[i] - mean_train) ** 2

    slope = a / b
    intercept = mean_ideal - (slope * mean_train)

    # step 3, calculate the RMSE and errors
    errors = []
    for i2 in range(length):
        y_pred = intercept + (slope * n_func_train[i2])
        z = abs(n_func_ideal[i2] - n_func_train[i2])
        errors = np.insert(errors, i2, z)
        rmse += (n_func_ideal[i2] - y_pred) ** 2
    # rmse = np.sqrt(rmse / length)
    print(rmse)

    rmse2 = sk.mean_squared_error(n_func_ideal, n_func_train)
    print(rmse2)

    return slope, intercept, errors, rmse
