# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 01:55:25 2019

@author: Mobasser
"""
import IPython
from scipy.io import wavfile
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
import librosa

wav_loc = "D:\Dell laptop\Projects\1.Stutter Stop\Makeathon\Code\s00.wav"
rate, data= wavfile.read(wav_loc)
data = data/32768
# from https://stackoverflow.com/questions/33933842/how-to-generate-noise-in-frequency-range-with-numpy
def fftnoise(f):
    f = np.array(f, dtype='complex')
    Np = (len(f) - 1) // 2
    phases = np.random.rand(Np) * 2 * np.pi
    phases = np.cos(phases) + 1j * np.sin(phases)
    f[1:Np+1] *= phases
    f[-1:-1-Np:-1] = np.conj(f[1:Np+1])
    return np.fft.ifft(f).real

def band_limited_noise(min_freq, max_freq, samples=1024, samplerate=1):
    freqs = np.abs(np.fft.fftfreq(samples, 1/samplerate))
    f = np.zeros(samples)
    f[np.logical_and(freqs>=min_freq, freqs<=max_freq)] = 1
    return fftnoise(f)

IPython.display.Audio(data=data, rate=rate)
fig, ax = plt.subplots(figsize=(20,4))
ax.plot(data)

