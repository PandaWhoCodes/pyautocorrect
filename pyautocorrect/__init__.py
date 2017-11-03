"""
Spell Corrector
Author: Thomas Ashish Cherian
https://github.com/PandaWhoCodes/pyautocorrect
"""

from pyautocorrect.checker import check


def correct(sentence):
    checker = check()
    checker.set_constants()
    return checker.correct_words(sentence)
