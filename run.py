import argparse
import importlib
from performance import list_runtimes

description = """
    Use --problem or -p to run the solution to a single problem,
    or use --performance-test or -t to run all problems and list
    the 10 slowest ones. I don't think anyone will ever use this
    option, but I use it a lot to make solutions faster. There's
    a pre-commit hook that run tests for all of them and I don't
    want it to take too much of my precious time.
"""

parser = argparse.ArgumentParser(
    prog="Henrique's Solutions for Project Euler",
    description=description,
    epilog="For entertainment and learning purposes only.",
)
parser.add_argument("-p", "--problem", required=False, type=int)
parser.add_argument("-t", "--performance-test", action="store_true")
args = parser.parse_args()

arguments_dict = vars(args)
problem_id = arguments_dict.get("problem")
if problem_id:
    problem_id = "{0:03n}".format(problem_id)
    module = importlib.import_module(problem_id)

    print(getattr(module, f"solution{problem_id}")())

if arguments_dict.get("performance_test"):
    list_runtimes()
