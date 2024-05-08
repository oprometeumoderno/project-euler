import os
import re
import importlib
import time
from tabulate import tabulate
from answers import get_answers


def list_runtimes():
    solution_modules = {}
    exec_times = []
    answers = get_answers()
    for solution in [f for f in os.listdir() if re.match(r"^\d{3}.py$", f)]:
        problem_id = solution.replace(".py", "")
        if problem_id in answers:
            solution_modules[problem_id] = importlib.import_module(problem_id)

            start = time.time()
            getattr(solution_modules[problem_id], f"solution{problem_id}")()
            end = time.time()
            exec_times.append((problem_id, round(end - start, 4)))

    exec_times = sorted(exec_times, key=lambda x: x[1], reverse=True)[:10]
    print(tabulate(exec_times, headers=["Problem ID", "Runtime (seconds)"]))
