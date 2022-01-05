#!/usr/bin/env python3
#
# Generates a best strategy for solving wordle

import sys

from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass


def read_puzzle_words(filename, word_len):
    words = list()
    with open(filename) as f:
        words = [w.rstrip() for w in f.readlines()]
    words = [w for w in words if len(w) == word_len and w.islower()]
    print(f"Read {len(words)} lower-case, {word_len} character words\n", file=sys.stderr)
    return words


def scored_heterograms(words):
    heterograms = [w for w in words if len(set(w)) == len(w)]
    letter_freq = OrderedCounter("".join(heterograms))
    word_scores = {h: sum([letter_freq[c] for c in h]) for h in heterograms}
    return OrderedDict(sorted(word_scores.items(), key=lambda s: s[1]))


def prompt(msg):
    try:
        resp = input(msg)
    except EOFError:
        return None
    return resp


def select_first_guess(words):
    first_guesses = scored_heterograms(words)
    guess = ""
    while True:
        guess = first_guesses.popitem()
        print(f"Guess is '{guess[0]}' (score={guess[1]})")
        resp = prompt("\nWas the guess accepted? (Y/N)\n")
        if len(resp) > 0 and resp[0].upper() == "Y":
            return guess


def read_guess(required_len):
    guess = ""
    while len(guess) != required_len:
        guess = prompt("\nEnter guess:\n")
    return guess


def main(word_file, puzzel_len):
    words = read_puzzle_words(word_file, puzzel_len)
    _ = select_first_guess(words)


if __name__ == "__main__":
    word_file = "/usr/share/dict/words"
    puzzel_len = 5
    try:
        main(word_file, puzzel_len)
    except KeyboardInterrupt:
        print("Exiting", file=sys.stderr)
