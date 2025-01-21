import matplotlib.pyplot as plt

def plot_graph(array_sizes, average_times, ascending_times, descending_times):
    plt.figure(figsize=(10, 6))
    plt.plot(array_sizes, average_times, label="Average Case", color='r', marker='o')
    plt.plot(array_sizes, ascending_times, label="Ascending Order", color='b', marker='o')
    plt.plot(array_sizes, descending_times, label="Descending Order", color='g', marker='o')

    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.title('Performance for Different Input Sizes')
    plt.legend()
    plt.grid(True)
    plt.show()