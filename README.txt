You have to write a program to efficiently compute discrete log in an additive group mod p.

Your program has to take two parameters, filePrime and exponentiationResult.

filePrime is a file containing only one line with (possibly very large) prime number.

exponentiationResult is a result of exponentiation g^x. Assuming g = 101 You have to find x.

Your program may be written in python, but doesn't have to be. discreteLog.py is an implementation of a naive discrete log algorithm in python. Python is a very good choice because it implements a reasonably good arbitrary precision bignum library.

the following is an example of running discreteLog.py, and checking the answer using checkAnswer.py:

$ python discreteLog.py smallPrime 42 
26288
$ python checkAnswer.py smallPrime 26288
42

Note that the result is what we started with, i.e. 42.

Throughout your implementation you may assume that g is always 101.
