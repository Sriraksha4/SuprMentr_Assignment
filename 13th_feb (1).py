import numpy as np

# Given temperature list
temp_list = [28, 32, 30, 37, 36, 38]

# Convert list to NumPy array
temps = np.array(temp_list)
print("Temperature Array:", temps)

# Maximum and Minimum temperature
print("Maximum Temp:", np.max(temps))
print("Minimum Temp:", np.min(temps))

# Average temperature
print("Average Temp:", np.mean(temps))

# Last 3 days temperature
print("Last 3 Days Temp:", temps[-3:])