#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write
from waves import sinusoid, square_wave, saw_tooth, wave_add, wave_diff

#Function to save waves as wav format audio file at 441.1 kHz sample rate
def wave_save(name, array):
	write(name+'.wav', 44100, array)

wavfile = read('vids/The_Boy_the_World_Forgot.wav')
song = wavfile[1]#time domain function
sample_rate = wavfile[0]#sampling rate from the wave file

#Save back song un-tampered 
#song_test = wave_save('test',song)

#First second of song (2d)
song_1d = song[:,0]

#Filter 
sin1 = sinusoid(60.,177.12,10000.)
filter_340 = sin1.sine_wave()

#print len(song_1d)/44100.
#print len(filter_340)/44100.

#Subtract out filter
filtered = wave_diff(song_1d, filter_340)

#FFT of 1st second of song
#ft_1d = np.fft.fft(song_1d)
#mag_1d = np.abs(ft_1d)

#FFT of 1st second of filtered song 
#ft_filt = np.fft.fft(filtered)
#mag_filt = np.abs(ft_filt)

filter_test = wave_save('filter_60hz',filtered)

'''
plt.subplot(211)
plt.plot(mag_1d)
plt.xlim(0,10000)

plt.subplot(212)
plt.plot(mag_filt)
plt.xlim(0,10000)

plt.show()
'''
