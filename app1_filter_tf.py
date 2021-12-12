from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


f0 = 5
w0 = 2*np.pi*f0
tf = signal.lti( [ 1/((w0)**2), 0,0 ], [ 1/((w0)**2), 1.414/(w0), 1 ] )

omega, gain, phase = tf.bode()

fig, plot_gain = plt.subplots()
fig.suptitle(r'Filtre coupe-bande')

color = 'tab:blue'
plot_gain.semilogx(omega, gain, color=color)
plot_gain.set_xlabel(r'Pulsation ($rad.s^{-1}$)')
plot_gain.set_ylabel("Gain (dB)", color=color)
plot_gain.tick_params(axis='y', labelcolor=color)

plot_gain.axvline(x=w0, color='black', linestyle='--')
plot_gain.text(w0, 2.5, r'$\omega_0 = 2\pi \times 100$', ha='center')#, transform=plot_gain.transAxes)

color = 'tab:red'
#plot_phase = plot_gain.twinx()
#plot_phase.semilogx(omega, phase, color=color)
#plot_phase.set_ylabel("Phase (°)", color=color)
#plot_phase.tick_params(axis='y', labelcolor=color)

plt.show()