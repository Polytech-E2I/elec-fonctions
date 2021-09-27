from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

tf = signal.lti([1/((200*np.pi)**2),0,1], [1/((200*np.pi)**2),9.9/(200*np.pi),1])

omega, gain, phase = tf.bode()

plt.semilogx(omega, gain)
plt.show()