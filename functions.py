import numpy as np
import sklearn.linear_model as skl
import sklearn.metrics as skm

def calc(n_func_train, n_func_ideal):

    # compute the amount of values:
    length = len(n_func_train)

    # calculate the mse
    mse = skm.mean_squared_error(n_func_ideal, n_func_train)

    # calculate slope and intercept
    n_func_ideal = n_func_ideal.reshape((-1, 1))
    reg = skl.LinearRegression().fit(n_func_ideal, n_func_train)
    intercept = reg.intercept_
    slope = reg.coef_

    # calculate the errors of the regression
    errors = []
    for i in range(length):
        y_pred = intercept + (slope * n_func_train[i])
        z = abs(y_pred - n_func_train[i])
        errors = np.insert(errors, i, z)

    return errors, mse
