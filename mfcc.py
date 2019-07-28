import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import rfft, irfft, fftfreq, fft
import scipy.fftpack
from scipy.io.wavfile import wav

N=40000
T=0.1
x = np.linspace(0.0,N*T,N)
(rate,data) = wav.read("D:\\Competition\\Makeathon\\Code\\s10(1).wav",mmap=True)
dataf = scipy.fftpack.fft(data[wl[0,0]:wl[0,1]])
