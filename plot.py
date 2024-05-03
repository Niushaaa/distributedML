import matplotlib.pyplot as plt

# Path to the file
file_path = 'training_time.txt'

# Lists to hold the extracted data
iteration_times = []
communication_times = []
ratios = []
losses = []

# Read from the file
try:
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into components
            sum_iter_time, sum_comm_time, ratio, loss = line.strip().split(',')
            # Convert strings to float
            sum_iter_time = float(sum_iter_time)
            sum_comm_time = float(sum_comm_time)
            ratio = float(ratio)
            loss = float(loss)
            # Append the data to the lists
            iteration_times.append(sum_iter_time)
            communication_times.append(sum_comm_time)
            ratios.append(ratio)
            losses.append(loss)
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
# Save the figure
save_path = 'training_time_analysis.png'  # Specify the path and filename here
plt.savefig(save_path, format='png', dpi=300)  # Save as PNG with high resolution

plt.show()

# plot another figure for losses
plt.figure(figsize=(10, 7))
plt.plot(losses, label='Loss')
plt.xlabel('Iteration')
plt.ylabel('Loss')
plt.title('Loss Analysis from File')
plt.legend()
# Save the figure
save_path = 'loss_analysis.png'  # Specify the path and filename here
plt.savefig(save_path, format='png', dpi=300)  # Save as PNG with high resolution

plt.show()
