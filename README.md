# Python Edinburgh Code Dojo, October 2018

The theme of the dojo was music.
We decided to convert text to music, with the most common letters in English becoming notes near the middle of the scale.
Note lengths are scaled so that each word takes the same time,
so short words sound slow, and long words make a quick flurry of notes.
A rest follows each word.

We used [PySynth](https://mdoege.github.io/PySynth/) to convert notes to wav files,
and then `aplay` to play the wav files. 

Ebooks were downloaded from [Project Gutenberg](http://www.gutenberg.org/). Shorter texts were from a variety of online sources.
