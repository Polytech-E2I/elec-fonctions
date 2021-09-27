from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


f0 = 100
w0 = 2*np.pi*f0
tf = signal.lti([1/((w0)**2),0,1], [1/((w0)**2),9.9/(w0),1])

omega, gain, phase = tf.bode()

plt.semilogx(omega, gain)
plt.title(r'Filtre coupe-bande $\omega_0 = 2\pi \times 100 rad.s^{-1}$')
plt.xlabel("Pulsation (rad/s)")
plt.ylabel("Gain (dB)")
plt.show()