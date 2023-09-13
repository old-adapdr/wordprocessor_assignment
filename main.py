"""File contains a WordAnalyzer container providing various methods"""
from collections import Counter
from typing import List, Tuple


class WordAnalyzer:
    """Provides methods to analyze a given text for occurances of words"""

    translator = str.maketrans({".": "", ",": ""})

    @staticmethod
    def max_frequency(text: str) -> int:
        """Returns the highest frequency of any word found in the text"""
        return max(
            Counter(
                text.translate(WordAnalyzer.translator).split()
            ).most_common(1)
        )[1]

    @staticmethod
    def get_frequency(text: str, word: str) -> int:
        """Returns the frequency of the specified word in the text"""
        return Counter(text.translate(WordAnalyzer.translator).split())[word]

    @staticmethod
    def get_frequency_listed(text: str, number: int) -> List[Tuple[str, int]]:
        """Returns a sorted list of {number} words ordered by frequency"""
        return Counter(
            text.translate(WordAnalyzer.translator).split()
        ).most_common(number)


with open("bacon.txt", "r") as file:
    text = file.read()
    print("max_frequency:", WordAnalyzer.max_frequency(text))
    print("get_frequency:", WordAnalyzer.get_frequency(text, "sirloin"))
    print("get_frequency_listed:", WordAnalyzer.get_frequency_listed(text, 3))
