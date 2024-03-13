from fitparse import FitFile
import os

# the overall max speed in meter p/s
max_speed = 0.0

# loop through all fit files in directory
for filename in os.listdir(os.path.abspath(os.getcwd())):
    if filename.endswith(".fit"):
        
        # open fitfile 
        fitfile = FitFile(filename)
        
        # Get all data messages that are of type record
        for record in fitfile.get_messages('record'):

            # Go through all the data entries in this record
            for record_data in record:

                if record_data.name == "enhanced_speed":
                    
                    # Check if record_data.value is a tuple
                    if isinstance(record_data.value, tuple):
                        # If it's a tuple, extract the first element as the float value
                        speed_value = record_data.value[0]
                    else:
                        # If it's not a tuple, directly assign it as the float value
                        speed_value = record_data.value
                    
                    # Check if speed_value is not None before comparing
                    if speed_value is not None and speed_value > max_speed:
                        max_speed = speed_value
    
    # continue if not a fit file
    else:
        continue
        
        
print("Your max speed in KM/H is " + str(max_speed * 3.6))
print("Your max speed in M/PH is " + str(max_speed * 2.237))