import argparse
import importlib
from performance import list_runtimes

parser = argparse.ArgumentParser(
    prog="Henrique's Solutions for Project Euler",
    description="literally what the title says",
    epilog="bottom text",
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
