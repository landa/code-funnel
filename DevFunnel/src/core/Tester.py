import unittest
import os

class Test(unittest.TestCase):

    def open_relative(self, what):
        return open(os.path.abspath(os.path.join(os.path.dirname(__file__),
            '..', 'tests', self.name(), what)))

    def setUp(self):
        from submission import answer
        self.answer = answer

    def tearDown(self):
        pass
    
    def check_answer(self, questionable_input):
        self.assertEqual(self.solution(questionable_input),
                         self.answer(questionable_input), 'wrong')
    
    def test_files(self):
        inputs = list()
        for files in os.walk('inputs'):
            for test_file in files[2]:
                inputs.append(test_file)
        for test_file in inputs:
            print "Processing input from '" + test_file + "'"
            yield self.single_file_test, test_file

    def single_file_test(self, which):
        question = eval(self.open_relative(os.path.join('inputs', which)).read())
        answer = self.answer(question)
        solution = eval(self.open_relative(os.path.join('outputs', which)).read())
        self.assertEqual(solution, answer, 'wrong')