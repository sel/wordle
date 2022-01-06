# Wordle Solver

Python solver for the [Wordle](https://www.powerlanguage.co.uk/wordle/) puzzel.


## Usage

```
$ ./solve.py
```
```
Read 12972 lower-case 5 character words

Next guess is 'soare' (score=16999)
Enter hint (gyx * 5) or nothing if guess was not accepted: xxyxx

Next guess is 'aalii' (score=22869)
Enter hint (gyx * 5) or nothing if guess was not accepted: ygyxx

Next guess is 'lanai' (score=22062)
Enter hint (gyx * 5) or nothing if guess was not accepted: ygggx

Next guess is 'canal' (score=20331)
Enter hint (gyx * 5) or nothing if guess was not accepted: xgggg

Next guess is 'banal' (score=19930)
Enter hint (gyx * 5) or nothing if guess was not accepted: ggggg
Congratulations!
```


## TODO

- [x] Sort word-list in `next_guess` by letter frequency, as already done for the first guess.
- [ ] See if there is a fancy data-structure that would improve performance.
- [ ] Add tests...
