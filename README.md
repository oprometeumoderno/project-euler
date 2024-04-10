# Introduction

[Project Euler](https://projecteuler.net) is an online platform that contains around one thousand problems intended to be solved with computer programs. The problems present an interesting intersection between mathematics and algorithms, providing challenges that span various domains in both fields. The platform also offers a collaborative forum where enthusiasts from all around the world share their thoughts and solutions (a discussion for a particular problem becomes available once the problem is solved).

I have a bachelor degree in computer science and, back when I was a student, I started solving these problems but they quickly progress into something that requires more mathematical knowledge than I had back then. Now that I am pursuing a degree in math, I re-discovered this challenge and once more started to work on the problems. I'll try to solve them all, but I am not sure how far I'll get.

# How to run it:

 The only requirement is Python (I use python 3.10.9), but don't forget to run
 `pip install -r requirements.txt` to install all requirements and
 `pre-commit install` to initialize the pre-commit hooks.

 After that, you can run a single solution by running
 `python run.py -p <problem_id>` where `problem_id` is the problem number.
 Example: `python run.py -p 45`.
 Tests are automated and run at every commit. There's also a pre-commit hook that
 runs `black` on modified files to linter them.

 ## Analyzing problem performance
 There's an option to run all problems at once and list the 10 slowest ones. It is `python run.py -t`. I don't think people will actually use this at all, but I use it a lot to make solutions faster and therefore saving time whenever unittest runs. It will output something like this:
```
Problem ID    Runtime (seconds)
------------  -------------------
       092              18.8423
       034              11.3672
       027               4.9794
       037               1.8677
       030               1.7468
       014               1.6722
       010               1.0345
       023               0.862
       047               0.7111
       050               0.6244
```

I'll try to solve at least the first 115 problems (thus getting into the 1% of PE's problems solvers), but it will be a long journey. I hope you can learn something from this repo.
