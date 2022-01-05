# Wordle Solver

Python solver for the [Wordle](https://www.powerlanguage.co.uk/wordle/) puzzel.


## Usage

```
$ ./solve.py
```
```
Read 8497 lower-case 5 character words

Guess is 'tarie' (score=10530)
Was the guess accepted? (Y/N) n
Guess is 'retia' (score=10530)
Was the guess accepted? (Y/N) y
Enter hint G/Y/X: yyyyx
23 words remaining in word-list

Next guess is 'inert'
Was the guess accepted? (Y/N) y
Enter hint G/Y/X: yxyyy
17 words remaining in word-list

Next guess is 'ticer'
Was the guess accepted? (Y/N) n

Next guess is 'tiger'
Was the guess accepted? (Y/N) y
Enter hint G/Y/X: ggggg
Congratulations!
```


## TODO

- [ ] Sort word-list in `next_guess` by letter frequency, as already done for the first guess.
- [ ] See if there is a fancy data-structure that would improve performance.
- [ ] Add tests...
