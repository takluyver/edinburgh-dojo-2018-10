from pathlib import Path
from subprocess import run, Popen, PIPE, DEVNULL

FREQUENCY = 'etaoinsrhdlucmfywgpbv'
ORDER = 'vpwfclhsiaetonrdumygb'

cache = Path('wordcache')

with open('./jekyll_hyde.txt', 'r') as fp:
    text = fp.read()


NOTES = (
    #'g2', 'a3', 'b3',
    'c3', 'd3', 'e3', 'f3', 'g3', 'a4', 'b4',
    'c4', 'd4', 'e4', 'f4', 'g4', 'a5', 'b5',
    'c5', 'd5', 'e5', 'f5', 'g6', 'a6', 'bb6',
)

def generate_words(text):
    paragraphs = text.lower().split('\n')
    for p in paragraphs:
        for word in p.split():
            yield word

import sys
sys.path.append('pysynth')
from pysynth_b import make_wav

def wav_for_word(word, fn):
    score = []
    word_notes = [NOTES[ORDER.index(c)] for c in word if c in ORDER]
    n = len(word_notes) + 1
    for note in word_notes:
        score.append((note, n))
    score.append(('r', n))
    
    make_wav(score[:10], bpm = 264, leg_stac = 0.9, boost=1.1, fn=fn, silent=True)

for word in generate_words(text):
    fn = cache / '{}.wav'.format(word)
    if not fn.is_file():
        wav_for_word(word, str(fn))

    print(word)
    aplay = run(['aplay', fn], stderr=DEVNULL, stdout=DEVNULL)
    
