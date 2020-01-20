from melopy.melopy import Melopy
from melopy import chords

# maj_C4 = chords.generateChord('maj', 'C4')
# maj_F4 = chords.generateChord('maj', 'F3')
# maj_G4 = chords.generateChord('maj', 'G3')
# print(maj_C4, maj_F4, maj_G4)

m = Melopy('mysong', tempo=360)
m.add_whole_note("E4")
m.add_half_note("E4")
m.add_half_note("G4")
m.add_half_note("E4")
m.add_half_note("D4")
m.add_whole_note("C4")
m.add_half_note("C4")
m.add_whole_note("B3")
m.add_half_note("B3")
m.render()