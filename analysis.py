import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("initial.dat", header=None, delim_whitespace=True)

print(df)
plt.plot(df.iloc[:, 0], df.iloc[:, 1])
plt.xlabel('energy')  # Replace 'Index' with your desired label for the x-axis
plt.ylabel('counts')  # Replace 'Value' with your desired label for the y-axis
plt.title('Plot Title')  # Replace 'Plot Title' with your desired title for the plot
# plt.xscale('log')  # Set y-axis scale to log
plt.yscale("log")
plt.gca().invert_yaxis()  # Invert y-axis

plt.show()