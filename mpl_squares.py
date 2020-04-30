import matplotlib.pyplot as plt

base = range(1, 1001)
squares = [each**2 for each in base]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.plot(base, squares, linewidth=3)
ax.scatter(base, squares, c=squares, cmap=plt.cm.Blues, s=100)


# Set chart title and label axes.
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Base", fontsize=14)
ax.set_ylabel("Square", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

ax.axis([0, 1100, 0, 1100000])

plt.show()

plt.savefig('pyplot.pdf', bbox_inches='tight')