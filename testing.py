""""Python scrip created for solving master examination (written assignment)

Lucas Correa Bornelli
Created in 07-10-2022 : 15:57

"""
import math
import numpy as np
import pandas as pd
import sqlalchemy
import functions


# initialization
def main():

    # create sql engine and connect to the database
    engine = sqlalchemy.create_engine('sqlite:///database.db')

    # Import CSV files and upload to the database
    train = pd.read_csv('train.csv')
    print(train)
    ideal = pd.read_csv('ideal.csv')
    test = pd.read_csv('test.csv')

    # create database tables and publish data
    train.to_sql('train', engine, if_exists='replace', index=False)
    ideal.to_sql('ideal', engine, if_exists='replace', index=False)
    test.to_sql('test', engine, if_exists='replace', index=False)

    # read the files from the database
    train = pd.read_sql('train', engine)
    ideal = pd.read_sql('ideal', engine)
    test = pd.read_sql('test', engine)

    # slice 'x' of train and ideal tables (as they are identical), convert all tables into numpy arrays
    x_values = train.iloc[:, 0].values
    train = train.iloc[:, 1:].values
    ideal = ideal.iloc[:, 1:].values
    test = test.iloc[:, :].values

    # for each y of the train functions, evaluate:
    for i in range(np.shape(train)[1]):
        n_func_train = train[:, i]

        mse_f = float('inf')  # reset the mse_f variable to be evaluated on the following iteration

        # for each y of the ideal functions, evaluate:
        for i1 in range(np.shape(ideal)[1]):
            n_func_ideal = ideal[:, i1]

            # call subroutine for performing the evaluation
            errors, mse = functions.calc(n_func_train, n_func_ideal)

            # if the current lse is smaller than the previous, update the variables and create the function matrix
            if mse < mse_f:
                mse_f = mse

                # create an array for storing the function index in an additional column
                i2 = len(n_func_train)
                func_index = np.full(i2, i1 + 1)

                # stores the last combination of two functions that satisfies the condition and the error (minimum MSE)
                pair_function = np.vstack((x_values, n_func_train, n_func_ideal, errors, func_index)).T

        # check the criterion for mapping the individual test cases
        for x in test:

            # lookup the line index on where the X value of the test matrix matches the X of the pair_function
            pos = np.where(pair_function[:, 0] == x[0])

            # use the found index for selecting the values to be evaluated
            delta_y = abs(x[1] - pair_function[pos, 1])
            if delta_y < (np.amax(pair_function[:, 3]) * math.sqrt(2)):
                test_data = np.concatenate((x, delta_y, pair_function[pos, 4]), axis=None)

        # combine the results into a final table
        if i == 0:
            test_data_f = test_data
        else:
            test_data_f = np.vstack((test_data_f, test_data))

    # format data to be saved in the database
    test_f = pd.DataFrame(test_data_f, columns=['X', 'Y', 'Delta Y', 'No. of ideal function'])
    test_f['No. of ideal function'] = 'N' + test_f['No. of ideal function'].astype(str)
    print(test_f)
    test_f.to_sql('test_data', engine, if_exists='replace', index=False)


if __name__ == '__main__':
    main()
