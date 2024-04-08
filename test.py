import unittest
import importlib

from answers import get_answers

ANSWERS = get_answers()


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution_modules = dict()
        self.answers = ANSWERS
        for problem_id in self.answers:
            self.solution_modules[problem_id] = importlib.import_module(problem_id)

    def get_answer(self, problem_id):
        return getattr(self.solution_modules[problem_id], f"solution{problem_id}")()

    def testProblem001(self):
        problem_id = "001"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem002(self):
        problem_id = "002"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem003(self):
        problem_id = "003"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem004(self):
        problem_id = "004"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem005(self):
        problem_id = "005"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem006(self):
        problem_id = "006"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem007(self):
        problem_id = "007"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem008(self):
        problem_id = "008"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem009(self):
        problem_id = "009"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem010(self):
        problem_id = "010"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem011(self):
        problem_id = "011"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem012(self):
        problem_id = "012"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem013(self):
        problem_id = "013"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem038(self):
        problem_id = "038"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))


if __name__ == "__main__":
    unittest.main()
