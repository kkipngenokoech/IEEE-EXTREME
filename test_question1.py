import unittest
from question1 import python_anagrams

class TestPythonAnagrams(unittest.TestCase):
    def test_single_word(self):
        self.assertEqual(python_anagrams(['word']), 1)

    def test_no_anagrams(self):
        self.assertEqual(python_anagrams(['word', 'hello', 'python']), 1)

    def test_some_anagrams(self):
        self.assertEqual(python_anagrams(['listen', 'silent', 'enlist', 'google', 'gogole']), 3)

    def test_all_anagrams(self):
        self.assertEqual(python_anagrams(['abc', 'bca', 'cab', 'bac', 'acb', 'cba']), 6)

    def test_empty_list(self):
        self.assertEqual(python_anagrams([]), 0)

    def test_mixed_case(self):
        self.assertEqual(python_anagrams(['Listen', 'Silent', 'Enlist', 'Google', 'Gogole']), 3)

if __name__ == '__main__':
    unittest.main()