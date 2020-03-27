#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------

import os
import sys
import logging


logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

# ----------------------------------------------------------------

from melopy.melopy import Melopy
from melopy import chords, scales, utility

# ----------------------------------------------------------------

def get_ticks(text, tick_size):
    return [text[i:i + tick_size] for i in range(0, len(text), tick_size)]

# ----------------------------------------------------------------

def main():
    songs_path = './songs/'
    os.makedirs(songs_path, exist_ok=True)
    
    songs = [{'name' : 'sevennationarmy',
              'notes': utility.iterate('G3', scales.SCALE_STEPS['major']),
              'tempo': 360,
              'text' : '515272524231322122515272524232423222'},
             {'name' : 'boomer',
              'notes': utility.iterate('D3', scales.SCALE_STEPS['harmonic_minor']),
              'tempo': 360,
              'text' : '223242625242322212223262524232'}]
    
    tick_size = 2
    
    for song in songs:
        logger.debug('Current song: {name}'.format(name=song['name']))
        logger.debug('Notes: {notes}'.format(notes=song['notes']))
        m = Melopy(songs_path + song['name'], tempo=song['tempo'])
        ticks = get_ticks(song['text'], tick_size)
        for tick in ticks:
            note = song['notes'][int(tick[0])]
            fraction = 1.0 / int(tick[1])
            logger.debug('{note} {fraction}'.format(note=note, fraction=fraction))
            m.add_fractional_note(note=note, fraction=fraction)
        m.render()

# ----------------------------------------------------------------

if __name__ == "__main__":
	main()
