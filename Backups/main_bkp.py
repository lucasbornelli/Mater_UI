""""Python scrip created for solving master examination (written assignment)

Lucas Correa Bornelli
Created in 07-10-2022 : 15:57

"""
import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sqlalchemy
import functions


# initialization
def main():
    # Import CSV files

    train = pd.read_csv('train.csv')
    ideal = pd.read_csv('ideal.csv')
    test = pd.read_csv('test.csv')

    # create sql engine and upload data into the database
    engine = sqlalchemy.create_engine('sqlite:///database.db')
    train.to_sql('train', engine, if_exists='replace', index=False)
    ideal.to_sql('ideal', engine, if_exists='replace', index=False)
    test.to_sql('test', engine, if_exists='replace', index=False)

    # read the database files
    train = pd.read_sql('train', engine)
    ideal = pd.read_sql('ideal', engine)
    test = pd.read_sql('test', engine)

    # exclude x0 of train and ideal (as they are identical)
    train = train.iloc[:, 1:].values
    ideal = ideal.iloc[:, 1:].values

    # for each y of the train functions, evaluate:
    for i in range(np.shape(train)[1]):
        n_func_train = train[:, i]

        rmse_f = float('inf')  # reset the rmse_f variable to be evaluated on the following iteration

        # for each y of the ideal functions, evaluate:
        for i1 in range(np.shape(ideal)[1]):
            n_func_ideal = ideal[:, i1]

            # call subroutine for performing the functions evaluations
            slope, intercept, errors, rmse = functions.calc(n_func_train, n_func_ideal)

            # if the current lse is smaller than the previous, update the variables and create the function matrix
            if rmse < rmse_f:
                slope_f, intercept_f, rmse_f = slope, intercept, rmse

                # stores the last combination of two functions that satisfies the condition and the error
                pair_function = np.vstack((n_func_train, n_func_ideal, errors)).T

        # initialize the all_functions variable for receiving all tables
        if i == 0:
            all_functions = pair_function
        else:
            all_functions = np.dstack((all_functions, pair_function))

    print(all_functions)
    # plotting the regression
    max_x = np.max(pair_function[:, 0])
    min_x = np.min(pair_function[:, 0])

    # calculating the regression line values
    x = np.linspace(min_x, max_x, 500)
    y = intercept_f + slope_f * x

    # plotting line
    plt.plot(x, y, label='Regression')

    # plotting scatter points
    plt.scatter(pair_function[:, 0], pair_function[:, 1], label='function')
    plt.show()


if __name__ == '__main__':
    main()
