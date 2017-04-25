import matplotlib.pyplot as plt
plt.plot(xData, yData)
plt.ylabel("My Dependant Data")
plt.xlabel("My Independant Data")
plt.title("My Title")
plt.plot()
plt.show()
# or to save the graph as a file
plt.savefig('path/graph.png')
