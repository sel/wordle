#!/usr/bin/env python3
#
# Wordle solver
# https://www.powerlanguage.co.uk/wordle/
#
# Copyright 2022 Steve Larkin
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import sys

from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass


def read_puzzle_words(filename, word_len):
    words = list()
    with open(filename) as f:
        words = [w.rstrip() for w in f.readlines()]
    words = [w for w in words if len(w) == word_len and w.islower()]
    print(f"Read {len(words)} lower-case {word_len} character words\n", file=sys.stderr)
    return words


def scored_heterograms(words):
    heterograms = [w for w in words if len(set(w)) == len(w)]
    letter_freq = OrderedCounter("".join(heterograms))
    word_scores = {h: sum([letter_freq[c] for c in h]) for h in heterograms}
    return OrderedDict(sorted(word_scores.items(), key=lambda s: s[1]))


def prompt(msg):
    try:
        return input(msg)
    except EOFError:
        return None


def prompt_to_continue():
    resp = prompt("Was the guess accepted? (Y/N) ")
    return len(resp) > 0 and resp[0].upper() == "Y"


def select_first_guess(words):
    first_guesses = scored_heterograms(words)
    guess = ""
    while True:
        guess = first_guesses.popitem()
        print(f"Guess is '{guess[0]}' (score={guess[1]})")
        if prompt_to_continue():
            return guess[0]


def read_hint(puzzel_len):
    hint = ""
    while len(hint) != puzzel_len or not set(hint).issubset({"G", "Y", "X"}):
        hint = prompt("Enter hint G/Y/X: ").upper()
    return hint


def next_guess(words, guess, hint):
    while True:
        for i, c in enumerate(guess):
            if hint[i] == "G":
                # Remove all words without c in pos i
                words = [w for w in words if w[i] == c]
            elif hint[i] == "Y":
                # Remove all words either missing c or with c in pos i
                words = [w for w in words if w[i] != c and c in w]
            else:
                # Remove all words containing c
                words = [w for w in words if c not in w]
        print(f"{len(words)} words remaining in word-list", file=sys.stderr)

        for w in words:
            print(f"\nNext guess is '{w}'")
            if prompt_to_continue():
                return words, w

        raise Exception("Unsolvable")


def main(word_file, puzzel_len):
    words = read_puzzle_words(word_file, puzzel_len)
    guess = select_first_guess(words)
    while True:
        hint = read_hint(puzzel_len)
        if hint == "G" * puzzel_len:
            print("Congratulations!")
            break
        words, guess = next_guess(words, guess, hint)


if __name__ == "__main__":
    word_file = "/usr/share/dict/words"
    puzzel_len = 5
    try:
        main(word_file, puzzel_len)
    except KeyboardInterrupt:
        print("\nExiting", file=sys.stderr)
