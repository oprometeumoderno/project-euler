import argparse
import importlib

parser = argparse.ArgumentParser(
    prog="Henrique's Solutions for Project Euler",
    description="literally what the title says",
    epilog="bottom text",
)
parser.add_argument("-p", "--problem", required=True, type=int)
args = parser.parse_args()

problem_id = "{0:03n}".format(vars(args).get("problem"))
module = importlib.import_module(problem_id)

print(getattr(module, f"solution{problem_id}")())
