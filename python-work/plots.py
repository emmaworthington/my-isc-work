import matplotlib.pyplot as plt

time = range(0, 7)
co2 = [250, 265, 272, 260, 300, 320, 389]
temp = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]

plt.plot(time, co2, '--b')
plt.plot(time, temp, '--r')
plt.title('$\mathregular{CO_2}$ concentration and temperature over time')
plt.ylabel('$\mathregular{CO_2}$ concentration (ppm)')
plt.xlabel('Time (decade)')
plt.pause(5)

plt.savefig('co2_temp.pdf')


