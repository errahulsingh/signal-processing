import numpy as np
import matplotlib.pyplot as plt

N = 1024    # number of samples

t = np.linspace(0, 5, N)    # time vector

signal = ([1] * 8 + [-1] * 8) * int(N/16)      # rectangular pulse

sample_rate = N/t[-1]     # calculated sample rate

f = sample_rate * np.arange(int(N/2)) / N   # frequency vector
fourier = np.fft.fft(signal)

# Plot signal
plt.figure()
plt.plot(t[0:50], signal[0:50])

# Plot fft
plt.figure()
plt.plot(f, np.abs(fourier[:int(N/2)]))

# Signal factorization
plt.figure()

plt.plot(t[0:25], signal[0:25])

for i in range(1,4):
    bottom = int(N/2 - (N/8 * i))
    top = int(bottom + N/8)

    fourier[bottom:top] = 0
    fourier[-top:-bottom] = 0

    signal_component_cut = np.fft.ifft(fourier)

    plt.plot(t[0:25],signal_component_cut[0:25])

# Show our figures
plt.show()