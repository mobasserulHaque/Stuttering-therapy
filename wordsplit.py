# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 13:16:06 2018

@author: Vedant_Tibrewal
"""

from pydub import AudioSegment
from pydub.silence import split_on_silence

sound_file = AudioSegment.from_wav("D:\\Competition\\Makeathon\\Code\\s00.wav")
audio_chunks = split_on_silence(sound_file, 
    # must be silent for at least half a second
    min_silence_len=500,

    # consider it silent if quieter than -16 dBFS
    silence_thresh=-16
)

for i, chunk in enumerate(audio_chunks):

    out_file = ".//splitAudio//chunk{0}.wav".format(i)
    print("exporting", out_file)
    chunk.export(out_file, format="wav")
