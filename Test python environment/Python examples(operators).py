# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 10:26:02 2022

"Comparators operations exercises"

@author: lucas
"""
def main():

    # Comparison of booleans
    print(True == False)

    # Comparison of integers
    print((-5*15) != 75)

    # Comparison of strings
    print("pyscript" == "PyScript")

    # Compare a boolean with an integer
    print(True == 1)
    "-----"
    # Comparison of integers
    x = -3 * 6
    print(x>=(-10))

    # Comparison of strings
    y = "test"
    print("test"<=y)

    # Comparison of booleans
    print(True>False)

    "------"

    # Create arrays
    import numpy as np
    my_house = np.array([18.0, 20.0, 10.75, 9.50])
    your_house = np.array([14.0, 24.0, 14.25, 9.0])

    # my_house greater than or equal to 18
    print(my_house>=18)
    
    # my_house less than your_house
    print(my_house<your_house)
    "------"   
    
    "___________________________________part1_____________________________________"

    # Define variables
    my_kitchen = 18.0
    your_kitchen = 14.0

    # my_kitchen bigger than 10 and smaller than 18?
    print(my_kitchen>10 and my_kitchen<18)

    # my_kitchen smaller than 14 or bigger than 17?
    print(my_kitchen<14 or my_kitchen>17)

    # Double my_kitchen smaller than triple your_kitchen?
    print((my_kitchen*2)< (your_kitchen*3))
    "------"   
    
    # Create arrays
    import numpy as np
    my_house = np.array([18.0, 20.0, 10.75, 9.50])
    your_house = np.array([14.0, 24.0, 14.25, 9.0])
    
    # my_house greater than 18.5 or smaller than 10
    print(np.logical_or(my_house>18.5, my_house<10))

    # Both my_house and your_house smaller than 11
    print(np.logical_and(my_house<11, your_house<11))
    "------"   
    
    "___________________________________part2_____________________________________"
    
    # Define variables
    room = "kit"
    area = 14.0

    # if statement for room
    if room == "kit" :
        print("looking around in the kitchen.")
    
    # if statement for area
    if area >15:
        print("big place!")
        
    "------"
    
    # Define variables
    room = "kit"
    area = 14.0
    
    # if-else construct for room
    if room == "kit" :
        print("looking around in the kitchen.")
    else :
        print("looking around elsewhere.")
    
    # if-else construct for area
    if area > 15 :
        print("big place!")
    else:
        print("pretty small.")
        
    "------"
    # Define variables
    room = "bed"
    area = 14.0

    # if-elif-else construct for room
    if room == "kit" :
        print("looking around in the kitchen.")
    elif room == "bed":
        print("looking around in the bedroom.")
    else :
        print("looking around elsewhere.")

    # if-elif-else construct for area
    if area > 15 :
        print("big place!")
    elif area >10:
        print("medium size, nice!")
    else :
        print("pretty small.") 
    "------"
    "___________________________________part3_____________________________________"
    
    # Import cars data
    import pandas as pd
    cars = pd.read_csv('cars.csv', index_col = 0)
    
    # Extract drives_right column as Series: dr
    dr = cars['drives_right']
    
    # Use dr to subset cars: sel
    sel = cars[dr]
    
    # Print sel
    print(sel)
    "------"
    
    # Import cars data
    import pandas as pd
    cars = pd.read_csv('cars.csv', index_col = 0)
    
    # Convert code to a one-liner
    
    sel = cars[cars['drives_right']]
    
    # Print sel
    print(sel)
    "------"
    
    # Import cars data
    import pandas as pd
    cars = pd.read_csv('cars.csv', index_col = 0)

    # Create car_maniac: observations that have a cars_per_cap over 500
    car_maniac=cars[cars['cars_per_cap']>500]

    # Print car_maniac
    print(car_maniac)
    "------"
    
    # Import cars data
    import pandas as pd
    cars = pd.read_csv('cars.csv', index_col = 0)
    
    # Import numpy, you'll need this
    import numpy as np
    
    # Create medium: observations with cars_per_cap between 100 and 500
    cpc = cars['cars_per_cap']
    medium = cars[np.logical_and(cpc>100, cpc<500)]
    
    # Print medium
    (medium)
    "------"
    
    "___________________________________part4_____________________________________"
    
    # Initialize offset
    offset = 8

    # Code the while loop

    while offset !=0 :
        print("correcting...")
        offset = offset-1
        print(offset)
    "------"
        
    
    # Initialize offset
    offset = -6
    
    # Code the while loop
    while offset != 0 :
        print("correcting...")
        if offset > 0 :
            offset = offset -1
        else : 
            offset = offset +1    
        print(offset)
    "------"
    
    # areas list
    areas = [11.25, 18.0, 20.0, 10.75, 9.50]

    # Code the for loop (elements is an arbitrary variable created for satisfying the for loop)
    for elements in areas :
        print(elements)
    "------"
    # areas list
    areas = [11.25, 18.0, 20.0, 10.75, 9.50]

    # Change for loop to use enumerate() and update print()
    for a, b in enumerate(areas) :
        print("room " + str(a) + ": " + str(b))

    #result:
    """room 0: 11.25
    room 1: 18.0
    room 2: 20.0
    room 3: 10.75
    room 4: 9.5"""
    
    "------"    
    # house list of lists
    house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
    # Build a for loop from scratch (print each line according to the index)
    for x in house:
        print("the " + str(x[0]) + " is " + str(x[1]) + " sqm")

    "------"        
    "___________________________________part5_____________________________________"
    
    # Definition of dictionary
    europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
    # Iterate over europe
    for key, value in europe.items():
        print("the capital of " + key + " is " + value)
    "------"
    
    # Import numpy as np
    import numpy as np
    np_height=[1,2,3]
    np_baseball=[1,2,3]

    # For loop over np_height
    for x in np_height:
        print(str(x) + " inches")

    # For loop over np_baseball (function to print all single elements of the 2D array individually)
    for y in np.nditer(np_baseball):
        print(str(y))
    
    "------"
    
    "___________________________________part_____________________________________"
    
    # Import cars data
    import pandas as pd
    cars = pd.read_csv('cars.csv', index_col = 0)

    # Iterate over rows of cars
    for a, b in cars.iterrows():
        print(a)
        print(b)
        
    #this iteration will print the combination of the first label (named variable a) and the line in sequence named variable b
    #cars_per_cap        country  drives_right
        #US            809  United States          True
        #AUS           731      Australia         False
        #JPN           588          Japan         False
        #IN             18          India         False
        #RU            200         Russia          True
        #MOR            70        Morocco          True
        #EG             45          Egypt          True
      
        #US
        #cars_per_cap              809
        #country         United States
        #drives_right             True
        #Name: US, dtype: object
        #AUS
        #cars_per_cap          731
        #country         Australia
        #drives_right        False
        #Name: AUS, dtype: object
        #JPN
        #cars_per_cap      588
        #country         Japan
        #drives_right    False
        #Name: JPN, dtype: object
        "------"
        
    # Import cars data
    import pandas as pd
    cars = pd.read_csv('cars.csv', index_col = 0)

    # Adapt for loop
    for lab, row in cars.iterrows() :
        print(lab + ": " + str(row[0]))
        
    #this example prints the same structure changed to the form: "US: 809"        
    "------"
    
    # Import cars data
    import pandas as pd
    cars = pd.read_csv('cars.csv', index_col = 0)
    
    # Code for loop that adds COUNTRY column
    for lab, row in cars.iterrows():
        cars.loc[lab, "COUNTRY"] = row["country"].upper()

    # Print cars
    print(cars)
    "------"
    # Import cars data
    import pandas as pd
    cars = pd.read_csv('cars.csv', index_col = 0)
    
    # Use .apply(str.upper)
    
    cars["COUNTRY"] = cars["country"].apply(str.upper)
    
    print(cars)
    
    "------"
    
    "___________________________________part n_____________________________________"
    # Import numpy and set seed
    import numpy as np
    np.random.seed(123)

    # Use randint() to simulate a dice (this will toss a coin between 1 and 6)
    print(np.random.randint(1,7))
    
    # Use randint() again for checking that the argument changed
    print(np.random.randint(1,7))
    
    "------"
    # NumPy is imported, seed is set

    # Starting step
    step = 50

    # Roll the dice
    dice = np.random.randint(1,7)
    
    # Finish the control construct
    if dice <= 2 :
        step = step - 1
    elif dice == (3,4,5) :
        step = step + 1
    else :
        step = step + np.random.randint(1,7)

    # Print out dice and step
    print(dice)
    print(step)
    
    "___________________________________part n_____________________________________"
    
    # NumPy is imported, seed is set

    # Initialize random_walk
    random_walk=[0]

    # Complete the ___
    for x in range(100) :
        # Set step: last element in random_walk
        step = random_walk[x]

        # Roll the dice
        dice = np.random.randint(1,7)

        # Determine next step
        if dice <= 2:
            step = step - 1
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # append next_step to random_walk
        random_walk.append(step)

    # Print random_walk
    print(random_walk)
    
    "------"
    # NumPy is imported, seed is set

    # Initialization
    random_walk = [0]

    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        random_walk.append(step)

    # Import matplotlib.pyplot as plt
    import matplotlib.pyplot as plt
    
    # Plot random_walk
    plt.plot(random_walk)
    
    # Show the plot
    plt.show()
    "------"
    # numpy and matplotlib imported, seed set.

    # initialize and populate all_walks
    all_walks = []
    for i in range(10) :
        random_walk = [0]
        for x in range(100) :
            step = random_walk[-1]
            dice = np.random.randint(1,7)
            if dice <= 2:
                step = max(0, step - 1)
            elif dice <= 5:
                step = step + 1
            else:
                step = step + np.random.randint(1,7)
            random_walk.append(step)
        all_walks.append(random_walk)

    # Convert all_walks to NumPy array: np_aw
    np_aw = np.array(all_walks)

    # Plot np_aw and show
    plt.plot(np_aw)
    plt.show()
    
    # Clear the figure
    plt.clf()
    
    # Transpose np_aw: np_aw_t
    np_aw_t = np.transpose(np_aw)
    
    # Plot np_aw_t and show
    plt.plot(np_aw_t)
    plt.show()
    "------"



    "------"
    
    
if __name__ == '__main__':
 main()
