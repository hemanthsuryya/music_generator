# python code to increase the pitch of .wav file by one scale

import wave
import contextlib
 
#read the wave file (mono)
with contextlib.closing(wave.open('C3.wav','r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    sound = f.readframes(frames)
 
#create a new file
with contextlib.closing(wave.open('C4.wav','w')) as f2:
    f2.setnchannels(1)
    f2.setsampwidth(2)
    f2.setframerate(rate*2)
    f2.writeframes(sound)