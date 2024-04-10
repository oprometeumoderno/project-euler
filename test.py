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

    def testProblem014(self):
        problem_id = "014"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem015(self):
        problem_id = "015"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem016(self):
        problem_id = "016"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem017(self):
        problem_id = "017"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem018(self):
        problem_id = "018"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem019(self):
        problem_id = "019"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem020(self):
        problem_id = "020"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem021(self):
        problem_id = "021"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem022(self):
        problem_id = "022"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem023(self):
        problem_id = "023"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem027(self):
        problem_id = "027"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem031(self):
        problem_id = "031"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem038(self):
        problem_id = "038"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem041(self):
        problem_id = "041"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem042(self):
        problem_id = "042"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem045(self):
        problem_id = "045"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem046(self):
        problem_id = "046"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem047(self):
        problem_id = "047"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem048(self):
        problem_id = "048"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem049(self):
        problem_id = "049"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))

    def testProblem050(self):
        problem_id = "050"
        self.assertEqual(self.answers[problem_id], self.get_answer(problem_id))


if __name__ == "__main__":
    unittest.main()
