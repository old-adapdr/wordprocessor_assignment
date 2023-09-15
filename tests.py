"""Files contains unittests for the WordAnalyzer"""
from typing import List, Tuple
from unittest import TestCase

from main import WordAnalyzer as WA


class WordAnalyzerTests(TestCase):
    """Container holding tests for the WordAnalyzer"""

    sample_text: str
    sample_list: List[Tuple[str, int]]

    def setUp(self):
        """Sets up test variables"""
        self.sample_text = "Beep beep beep, Boop boop, blip blop"
        self.sample_list = [("beep", 3), ("boop", 2)]

    def test_max_frequency(self):
        max_frequency = WA.max_frequency(self.sample_text)
        self.assertEqual(3, max_frequency)

    def test_get_frequency(self):
        frequency = WA.get_frequency(self.sample_text, "boop")
        self.assertEqual(2, frequency)

    def test_get_frequency_listed(self):
        frequency_listed = WA.get_frequency_listed(self.sample_text, 2)
        self.assertEqual(self.sample_list, frequency_listed)

    def test_extra(self):
        """
        For input text “The sun shines over the lake” and n = 3,
        it should return the list { (“the”, 2), (“lake”, 1), (“over”, 1) }
        """
        most_frequent_n_words = WA.get_frequency_listed(
            "The sun shines over the lake", 3
        )
        expected_assignment_example = [("the", 2), ("lake", 1), ("over", 1)]
        self.assertEqual(expected_assignment_example, most_frequent_n_words)
