import matplotlib.pyplot as plt
plt.figure(1)
plt.plot([1,2,3,4,5]) 
plt.show(block=False)

# Create a new figure to show the extra information.
# http://matplotlib.org/users/pyplot_tutorial.html#working-with-multiple-figures-and-axes
plt.figure(2)
plt.plot([2,2,2,2,2]) 
plt.show()
