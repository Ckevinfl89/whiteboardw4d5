from whiteboard import solution
from unittest import TestCase, main


class TestWhiteboard(TestCase):

    def test_anagrams1(self):
        s, t = "anagram", "nagaram"
        self.assertTrue(solution(s, t))

    def test_not_anagrams1(self):
        s, t = "stops", "pots"
        self.assertFalse(solution(s, t))

    def test_not_anagrams2(self):
        s, t = "rat", "car"
        self.assertFalse(solution(s, t))

    def test_not_anagrams3(self):
        s, t = "hello", "world"
        self.assertFalse(solution(s, t))

    def test_different_lengths(self):
        s, t = "abcd", "abc"
        self.assertFalse(solution(s, t))

    def test_caps(self):
        s, t = "RACEcar", "raceCAR"
        self.assertTrue(solution(s, t))

if __name__ == "__main__":
    main()