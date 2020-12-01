1-1 scans from either end of a sorted list, which appears to not make any difference at this size of problem:

```
doc@lion:~/git/adventofcode/2020/1$ time python 1-1-straight.py input.txt 
252 + 1768 == 2020 (product: 445536)

real	0m0.026s
user	0m0.022s
sys	0m0.005s

doc@lion:~/git/adventofcode/2020/1$ time python 1-1.py input.txt 
252 + 1768 == 2020 (product: 445536)

real	0m0.019s
user	0m0.012s
sys	0m0.008s
```

Similarly, not sorting and going straight in brute force also has negligible outcomes
(although it happened to be faster on this run so ¯\\_(ツ)_/¯)

```
doc@lion:~/git/adventofcode/2020/1$ time python 1-1-unsorted.py input.txt 
1768 + 252 == 2020 (product: 445536)

real	0m0.018s
user	0m0.011s
sys	0m0.007s
```


