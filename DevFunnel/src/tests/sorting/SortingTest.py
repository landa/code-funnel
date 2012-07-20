from core import Tester
import random
import nose

class SortingTest(Tester.Test):
    '''
    Simple sorting test
    '''
    
    def name(self):
        '''The name of the test.'''
        return 'sorting'
    
    def solution(self, unsorted):
        '''An implementation of the correct solution.'''
        return sorted(unsorted)
    
    def test_files_enabled(self):
        '''Delete this method if you don't want to run file tests.'''
        yield self.test_files
    
    ## Custom tests #####
    
    def test_simple(self):
        unsorted = range(1, 6)
        self.check_answer(unsorted)
    
    def test_random(self):
        unsorted = range(100)
        random.shuffle(unsorted)
        self.check_answer(unsorted)

if __name__ == "__main__":
    nose.main()