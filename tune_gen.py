# write python code to generate original music tunes in melancholic genre

import random
import pygame

pygame.init()

# define notes
notes = ["C3","D3","E3","F3","G3","A3","B3","C3","D4","E4","F4","G4","A4","B4","C5","D5","E5","F5","G5","A5","B5","C6"]

# define melancholic scale
scale = ["C3","D3","E3","F3","G3","A3","B3","C3"]

# define melancholic rhythm
rhythm = [0.125, 0.125, 0.125, 0.125, 0.25, 0.25, 0.125, 0.25]

# define tempo
tempo = 90

# generate random melancholic melody
melody = []
for i in range(50):
    melody.append(random.choice(scale))

# play the melody
for note in melody:
    print(note)
    pygame.mixer.music.load('./key_notes/'+str(note)+'.wav')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(10)