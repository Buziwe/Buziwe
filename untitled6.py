# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 19:23:06 2020

@author: 212560141
"""

# Import provided tire value list
sensor_readings = clusterSensor

# Create fake readings that are in range to demonstrate secondary condition.
acceptable_sensor_readings = [random.random() for i in range(1,17)]
# Define acceptable tire pressure range
acceptable_range = range(0,1)

# Define function, takes input of numbers as a list
def check_sensor_readings(clusterSensor):
    # Print out current readings
    print('Current sensor readings: {}'.format(sensor_reading_list_of_numbers))
    # Create a new list to hold the readings that are out of acceptable range
    number_of_sensor_out_of_range = []
    # Iterate through the list of tire readings. Use enumerate to get index and value
    for i, number in enumerate(clusterSensor):
        # Check if the number is witin the specified range
        if number <= acceptable_range[1] or number >= acceptable_range[0]:
            # Add number to the out of range list
            number_of_tires_out_of_range.append(number)
            # Set variable to tell us that pressures are not acceptable
            tire_pressures_acceptable = False
            # Check if numbers are over or under the acceptable range and print correct statement
            if number < 32:
                number = 32 - number
                print('Tire {} is {}psi under the acceptable limit'.format(i,number))
            elif number > 32:
                number = number - 32
                print('Tire {} is {}psi over the acceptable limit'.format(i,number))
        # In numbers aren't out of acceptable range set tire pressures acceptable variable to True
        else:
            tire_pressures_acceptable = True
    # Print if tires are in acceptable range or how many are not in the acceptable range
    if tire_pressures_acceptable == True:
        print('All tire pressures are within the acceptable range')
    else:
        print('{} tires have pressures out of the acceptable range'.format(len(number_of_tires_out_of_range)))

# Call the function twice to demonstrate acceptable and unacceptable readings
check_tire_readings(tire_readings)

check_tire_readings(acceptable_tire_readings)

i == float("err")