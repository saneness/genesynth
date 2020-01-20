#!/usr/bin/env python
# -*- coding: utf-8 -*-

from melopy.melopy import Melopy
from melopy import chords, scales, utility


def get_ticks(text, tick_size):
        return [text[i:i + tick_size] for i in range(0, len(text), tick_size)]


songs = [{'name' : 'sevennationarmy',
          'notes': utility.iterate('G3', scales.SCALE_STEPS['major']),
          'tempo': 360,
          'text' : '152527252413231222' * 2},
         {'name' : 'boomer',
          'notes': utility.iterate('D3', scales.SCALE_STEPS['harmonic_minor']),
          'tempo': 360,
          'text' : '222324262524232221222326252423'}]

tick_size = 2

for song in songs:
        m = Melopy(song['name'], tempo=song['tempo'])
        ticks = get_ticks(song['text'], tick_size)
        print(ticks)
        for tick in ticks:
                note = song['notes'][int(tick[1])]
                fraction = 1.0 / int(tick[0])
                m.add_fractional_note(note=note, fraction=fraction)
        m.render()