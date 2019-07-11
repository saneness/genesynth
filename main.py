from melopy import chords, Melopy

maj_C4 = chords.generate_chord('maj', 'C4')
maj7_C4 = chords.generate_chord('maj7', 'C4')
aug_C4 = chords.generate_chord('aug', 'C4')

m = Melopy('mysong', sound_type='piano')
m.add_half_note(maj_C4)
m.add_half_note(maj7_C4)
m.add_half_note(aug_C4)
m.render()
m.play()