import sys

FREQUENCY = 'etaoinsrhdlucmfywgpbv'
ORDER = 'vpwfclhsiaetonrdumygb'

with open(sys.argv[1], 'r') as fp:
    text = fp.read()

wav_filename = sys.argv[1].split('.')[0] + '.wav'

NOTES = (
    'c3', 'd3', 'e3', 'f3', 'g3', 'a4', 'b4',
    'c4', 'd4', 'e4', 'f4', 'g4', 'a5', 'b5',
    'c5', 'd5', 'e5', 'f5', 'g6', 'a6', 'b6',
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

sys.path.append('pysynth')
from pysynth_b import make_wav
make_wav(score[:500], bpm = 264, leg_stac = 0.9, boost=1.1, fn=wav_filename)
