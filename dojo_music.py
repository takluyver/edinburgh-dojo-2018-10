from pysynth_b import make_wav

# Example 1: The C major scale
song1 = [
    ['c',4],['d',4],['e',4],['f',4],['g',4],['a',4],['b',4],['c5',2],['r',1],
    ['c3',4],['d3',4],['e3',4],['f3',4],['g3',4],['a3',4],['b3',4],['c4',2],['r',1],
    ['c1*', 1], ['c2*', 1], ['c3*', 1], ['c4*', 1], ['c5*', 1], ['c6*', 1], ['c7*', 1], ['c8*', 1],
]


make_wav(song1, bpm = 132/2, leg_stac = 0.9, boost=1.1, fn="dojo_music.wav")
