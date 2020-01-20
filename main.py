#!/usr/bin/env python
# -*- coding: utf-8 -*-

from melopy.melopy import Melopy
from melopy import chords, scales, utility

notes = utility.iterate('G3', scales.SCALE_STEPS['major'])
tempo = 360

tick_size = 2
song = '152527252413231222' * 2 # seven nation army
song = [song[i:i + tick_size] for i in range(0, len(song), tick_size)]
duration = len(song)

print(notes)
print(song)
print(duration)

m = Melopy('mysong', tempo=tempo)
for i in range(duration):
        tick = song[i]
        note = notes[int(tick[1])]
        fraction = 1.0 / int(tick[0])
        m.add_fractional_note(note=note, fraction=fraction)

m.render()