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
        self.sample_list = [("beep", 2), ("Beep", 1)]

    def test_max_frequency(self):
        max_frequency = WA.max_frequency(self.sample_text)
        self.assertEqual(2, max_frequency)

    def test_get_frequency(self):
        frequency = WA.get_frequency(self.sample_text, "beep")
        self.assertEqual(2, frequency)

    def test_get_frequency_listed(self):
        frequency_listed = WA.get_frequency_listed(self.sample_text, 2)
        self.assertEqual(self.sample_list, frequency_listed)
