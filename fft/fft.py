import numpy as np
import matplotlib.pyplot as plt

N = 1024    # number of samples
freq1 = 5    # first signal frequency in Hz
freq2 = 40    # second signal frequency in Hz
freq3 = 70    # thrid signal frequency in Hz

t = np.linspace(0, 5, N)    # time vector
signal = np.sin((freq1 * 2 * np.pi) * t) + np.sin((freq2 * 2 * np.pi) * t) + np.sin((freq3 * 2 * np.pi) * t)      #signal vector

#signal = ([1] * 8 + [0] * 8) * 64      # rectangular pulse

sample_rate = N/t[-1]     # calculated sample rate

f = sample_rate * np.arange(int(N/2)) / N   # frequency vector
fourier = np.fft.fft(signal)


plt.plot(f, np.abs(fourier[:int(N/2)]))
plt.show()