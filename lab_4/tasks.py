 TASKS (9p)
#1 Looking at the Euler method above create your own function which takes:
# a (from x' = ax)
# h - step
# T time range
# as an input and plots the solution of a differential equation x' = ax (1p)
#2 Beside the solution print the 'ideal' approximation on your chart using for example green color as a reference. (1p)
#2 Hint: use small step value. Use plt.legend to explain which serie is the 'ideal'
#3 Find a differential equation which represents a process / model (your choice) and implement it using odeint python function (1p)
#4 Look at the example of optimization for exponential function.
# Did you encounter any errors? Where in code do we display the optimal point? Do we minimize or maximize and which function?
# Start your search always from the point (0, -2). (1p)
#5 Create your own 3d function with multiple local optima.
# Create an algorithm which takes an initial point and looks for the closest local optimum (1p)
# Create an algorithm which aims to find a global optimum, the time of execution is limiter to ~30sec (1p)
# If your solution is heuristic test its quality. Measure the probability of finding the GLOBAL optimum (1p).
# You can, for example, execute your search function multiple times and check if the returned result is what you expected.
# Measure the success / total trials rate (2p).