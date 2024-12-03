import math
import random
import matplotlib.pyplot as plt
import numpy as np

# Function to perform basic factorization using Trial Division
def basic_factorization(n):
    factors = []
    for divisor in range(2, int(math.sqrt(n)) + 1):
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
    if n > 1:  # If remaining n is greater than 1, it's prime
        factors.append(n)
    return factors

# Pollard's Rho Factorization Algorithm
def rho_factorization(n):
    if n % 2 == 0:
        return 2
    x = random.randint(2, n - 1)
    y = x
    c = random.randint(1, n - 1)
    g = 1
    while g == 1:
        x = (x**2 + c) % n
        y = (y**2 + c) % n
        y = (y**2 + c) % n
        g = math.gcd(abs(x - y), n)
    return g

# Data for graph generation: Number sizes and execution times (hypothetical values for demonstration)
input_sizes = [10**2, 10**4, 10**6, 10**8]  # Example input sizes
basic_method_times = [0.01, 10, 1000, 100000]  # Hypothetical times in seconds
rho_method_times = [0.001, 1, 100, 10000]
gnfs_method_times = [0.0001, 0.1, 10, 1000]

# Plotting the data
def generate_graph():
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, basic_method_times, label="Basic Factorization", marker='o')
    plt.plot(input_sizes, rho_method_times, label="Rho Factorization", marker='s')
    plt.plot(input_sizes, gnfs_method_times, label="GNFS", marker='^')

    # Logarithmic scale for better visualization
    plt.xscale('log')
    plt.yscale('log')

    # Labels and title for the graph
    plt.title("Execution Time of Integer Factorization Methods", fontsize=14)
    plt.xlabel("Input Size (N)", fontsize=12)
    plt.ylabel("Execution Time (seconds)", fontsize=12)
    plt.legend()
    plt.grid(True, which="both", linestyle='--', linewidth=0.5)

    # Save the graph as a PNG file
    plt.savefig("factorization_execution_time_graph.png", dpi=300)

    # Display the plot
    plt.tight_layout()
    plt.show()

# Example usage of the factorization algorithms and graph generation
def main():
    num_to_factor = 187  # Example number for factorization
    print(f"Number to factor: {num_to_factor}")
    
    # Trial Division Method
    print("Performing Basic Factorization:")
    trial_factors = basic_factorization(num_to_factor)
    print(f"Factors: {trial_factors}")
    
    # Pollard's Rho Method
    if len(trial_factors) == 1:  # Only apply Pollard's Rho if Trial Division doesn't fully factorize
        print("Using Rho Factorization:")
        factor = rho_factorization(num_to_factor)
        print(f"One factor: {factor}, Remaining: {num_to_factor // factor}")
    
    # Generate the execution time graph
    generate_graph()

if __name__ == "__main__":
    main()
