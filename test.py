import unittest
import importlib


# print(getattr(module, f"solution{problem_id}")())

ANSWERS = {"001": 233168}


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution_modules = dict()
        self.answers = ANSWERS
        for problem in range(1, 4):
            problem_id = "{0:03n}".format(problem)
            self.solution_modules[problem_id] = importlib.import_module(problem_id)

    def get_answer(self, problem_id):
        return getattr(self.solution_modules[problem_id], f"solution{problem_id}")()

    def testProblem001(self):
        problem_id = "001"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))


if __name__ == "__main__":
    unittest.main()
