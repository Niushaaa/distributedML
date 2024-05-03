import matplotlib.pyplot as plt

# Path to the file
file_path = 'training_time.txt'

# Lists to hold the extracted data
iteration_times = []
communication_times = []
ratios = []

# Read from the file
try:
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into components
            sum_iter_time, sum_comm_time, _ = line.strip().split(',')
            # Convert strings to float
            sum_iter_time = float(sum_iter_time)
            sum_comm_time = float(sum_comm_time)
            # Append the data to the lists
            iteration_times.append(sum_iter_time)
            communication_times.append(sum_comm_time)
            # Calculate the ratio and handle division by zero
            ratio = sum_comm_time / sum_iter_time if sum_iter_time != 0 else 0
            ratios.append(ratio)
except FileNotFoundError:
    print("The file does not exist. Please check the file path and name.")

# Plotting the data
plt.figure(figsize=(10, 7))
plt.plot(iteration_times, label='Sum Iteration Time')
plt.plot(communication_times, label='Sum Communication Time')
plt.plot(ratios, label='Ratio of Communication to Iteration Time')
plt.xlabel('Iteration')
plt.ylabel('Time (s)')
plt.title('Training Time Analysis from File')
plt.legend()
plt.show()
