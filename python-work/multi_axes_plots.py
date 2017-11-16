import matplotlib.pyplot as plt

time = range(0, 7)
co2 = [250, 265, 272, 260, 300, 320, 389]
temp = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(time, co2, '--b')
ax2.plot(time, temp, '--r')
plt.title('$\mathregular{CO_2}$ concentration and temperature over time')
ax1.set_ylabel('$\mathregular{CO_2}$ concentration (ppm)')
ax2.set_ylabel('Temperature ($\mathregular{^{\circ}C}$)')
ax1.set_xlabel('Time (decade)')
plt.pause(10)

plt.savefig('co2_temp2.pdf')
