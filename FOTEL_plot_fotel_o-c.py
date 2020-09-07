import numpy as np
import matplotlib.pyplot as plt

mjd, K, phase, oc3 = np.loadtxt('FOTEL/nugem.o-c', skiprows=1, unpack=True)
zero_point = 0

# mjd, rv = np.loadtxt('RVs_rivi_email.dat', skiprows=2, unpack=True)

plt.scatter(phase, K + zero_point, marker='+', color='black', label='RV')
# plt.scatter(phase-1, K + zero_point, marker='+', color='black')
# plt.scatter(phase+1, K + zero_point, marker='+', color='black')

plt.scatter(phase, K-oc3 + zero_point, marker='+', color='red', label='solution')
# plt.scatter(phase-1, K-oc3 + zero_point, marker='+', color='red')
# plt.scatter(phase+1, K-oc3 + zero_point, marker='+', color='red')

# plt.scatter(phase, oc3, marker='x', s=10, color='black', label='O-C')
# plt.scatter(phase-1, oc3, marker='+', color='black')
# plt.scatter(phase+1, oc3, marker='+', color='black')

plt.axhline(y=0, ls=':', color='black')

plt.xlabel('P')
plt.ylabel('RV [km/s]')
plt.xlim(-0.1, 1.1)
# plt.ylim(-30, 30)
plt.legend(fontsize=8)
# plt.savefig('RV_O-C.png', format='png', dpi=150)
plt.show()

