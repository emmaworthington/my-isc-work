import matplotlib.pyplot as plt

plt.subplot(1, 3, 1)
plt.plot(range(0, 10, 1))

plt.subplot(1, 3, 2)
plt.plot(range(10, 0, -1))

plt.subplot(1, 3, 3)
plt.plot([4] * 10)

plt.pause(15)
