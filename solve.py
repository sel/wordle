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
    print(f"Read {len(words)} lower-case {word_len} character words", file=sys.stderr)
    return words


def words_by_letter_frequency(word_list):
    letter_freq = OrderedCounter("".join(word_list))
    word_scores = {h: sum([letter_freq[c] for c in h]) for h in word_list}
    return OrderedDict(sorted(word_scores.items(), key=lambda s: s[1]))


def read_hint(puzzel_len):
    while True:
        hint = input(f"Enter hint (gyx * 5) or nothing if guess was not accepted: ").lower()
        if len(hint) == 0:
            return None
        elif len(hint) == puzzel_len and set(hint).issubset({"g", "y", "x"}):
            return hint


def next_guess(word_list, puzzel_len):
    unacceptable = []
    while len(word_list) > 0:
        guess = word_list.popitem()
        print(f"\nNext guess is '{guess[0]}' (score={guess[1]})")
        hint = read_hint(puzzel_len)
        if hint:
            return guess[0], hint, unacceptable
        else:
            unacceptable += guess
    raise Exception("unsolvable: exhausted the word-list")


def apply_hint(ordered_words, guess, hint, unacceptable):
    words = [w for w in ordered_words.keys() if w not in unacceptable]
    for i, c in enumerate(guess):
        if hint[i] == "g":
            words = [w for w in words if w[i] == c]
        elif hint[i] == "y":
            words = [w for w in words if c in w and w[i] != c]
        elif hint[i] == "x":
            # FIXME(sel): Limit grey(x) processing to the case when there is only one occurrence
            # of c in guess.  Otherwise by simply removing all words containing c would we would
            # fail in the case where there are multiple occurrences of c in guess with a mixture of
            # green and grey.
            if guess.count(c) == 1:
                words = [w for w in words if c not in w]
        # print(f"{len(words)} words remaining in word-list after applying hint {i}={hint[i]} to guess {guess}.",
        #       f"Head={list(reversed(words[-5:]))}", file=sys.stderr)
    return OrderedDict([(w, ordered_words[w]) for w in words])


def main(word_file, puzzel_len):
    all_words = read_puzzle_words(word_file, puzzel_len)
    ordered_words = words_by_letter_frequency(all_words)
    heterograms = [w for w in all_words if len(set(w)) == len(w)]
    ordered_heterograms = words_by_letter_frequency(heterograms)

    guess, hint, unacceptable = next_guess(ordered_heterograms, puzzel_len)
    while True:
        if hint == "g" * puzzel_len:
            print("Congratulations!")
            break
        ordered_words = apply_hint(ordered_words, guess, hint, unacceptable)
        guess, hint, unacceptable = next_guess(ordered_words, puzzel_len)


if __name__ == "__main__":
    word_file = "/usr/share/dict/words"
    puzzel_len = 5
    try:
        main(word_file, puzzel_len)
    except KeyboardInterrupt:
        print("\nExiting", file=sys.stderr)
