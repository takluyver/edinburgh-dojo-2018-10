FREQUENCY = 'etaoinsrhdlucmfywgpbv'
ORDER = 'vpwfclhsiaetonrdumygb'



with open('./theTruants.txt', 'r') as fp:
    text = fp.read()


NOTES = (
    #'g2', 'a3', 'b3',
    'c3', 'd3', 'e3', 'f3', 'g3', 'a4', 'b4',
    'c4', 'd4', 'e4', 'f4', 'g4', 'a5', 'b5',
    'c5', 'd5', 'e5', 'f5', 'g6', 'a6', 'bb6',
)

def generate_music(text):
    paragraphs = text.lower().split('\n')
    for p in paragraphs:
        for word in p.split():
            yield [NOTES[ORDER.index(c)] for c in word if c in ORDER]
            
score = []
for word_notes in generate_music(text):
    n = len(word_notes) + 1
    #print(word_notes)
    for note in word_notes:
        score.append((note, n))
    score.append(('r', n))

import sys
sys.path.append('pysynth')
from pysynth_b import make_wav
make_wav(score[:100], bpm = 132, leg_stac = 0.9, boost=1.1, fn="book.wav")
