import numpy as np

# Read the function to be transformed from the user
func_str = input("Enter a function of t (in terms of t and any variables you want to define): ")

# Read the variables and their values from the user
variables = {}
while True:
  var_str = input("Enter a variable and its value (e.g., a=1), or leave blank to continue: ")
  if not var_str:
    break
  var, val = var_str.split('=')
  variables[var] = eval(val)

# Define the function using a lambda function
func = lambda t: eval(func_str, variables, {'t': t})

# Read the range of the transformation from the user
t_start = float(input("Enter the start value for t: "))
t_end = float(input("Enter the end value for t: "))

# Calculate the Fourier transform of the function
t = np.linspace(t_start, t_end, 1000)
f = func(t)
F = np.fft.fft(f)

# Print the result
print("The Fourier transform of the function is:")
print(F)
