import numpy as np
import matplotlib.pyplot as plt

N = 1024    # number of samples
freq1 = 5    # first signal frequency in Hz
freq2 = 10    # second signal frequency in Hz
freq3 = 20    # thrid signal frequency in Hz

t = np.linspace(0, 5, N)    # time vector
signal = np.sin((freq1 * 2 * np.pi) * t) + np.sin((freq2 * 2 * np.pi) * t) + np.sin((freq3 * 2 * np.pi) * t)      # signal vector

sample_rate = N/t[-1]     # calculated sample rate

f = sample_rate * np.arange(int(N/2)) / N   # frequency vector
fourier = np.fft.fft(signal)

# Plot signal
plt.figure()
plt.plot(t, signal)

# Plot fft
plt.figure()
plt.plot(f, np.abs(fourier[:int(N/2)]))

# Cut 10 Hz frequency
fourier[40:70] = 0
fourier[-70:-40] = 0

# And plot modified fft
plt.figure()
plt.plot(f, np.abs(fourier[:int(N/2)]))

# Inverse fft
modified_signal = np.fft.ifft(fourier)

# Plot modified signal
plt.figure()
plt.plot(t, modified_signal)

# Show our figures
plt.show()