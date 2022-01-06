# Wordle Solver

Python solver for the [Wordle](https://www.powerlanguage.co.uk/wordle/) puzzel.


## Usage

```
$ ./solve.py
```
```
Read 8497 lower-case 5 character words

Next guess is 'tarie' (score=10530)
Enter hint (gyx * 5) or nothing if guess was not accepted:

Next guess is 'retia' (score=10530)
Enter hint (gyx * 5) or nothing if guess was not accepted: xxxxy

Next guess is 'amaas' (score=17085)
Enter hint (gyx * 5) or nothing if guess was not accepted:

Next guess is 'oasal' (score=16486)
Enter hint (gyx * 5) or nothing if guess was not accepted:

Next guess is 'salal' (score=16053)
Enter hint (gyx * 5) or nothing if guess was not accepted: xgxgg

Next guess is 'oadal' (score=15502)
Enter hint (gyx * 5) or nothing if guess was not accepted:

Next guess is 'canal' (score=15062)
Enter hint (gyx * 5) or nothing if guess was not accepted: xgggg

Next guess is 'manal' (score=14817)
Enter hint (gyx * 5) or nothing if guess was not accepted:

Next guess is 'banal' (score=14678)
Enter hint (gyx * 5) or nothing if guess was not accepted: ggggg
Congratulations!
```


## TODO

- [x] Sort word-list in `next_guess` by letter frequency, as already done for the first guess.
- [ ] See if there is a fancy data-structure that would improve performance.
- [ ] Add tests...
