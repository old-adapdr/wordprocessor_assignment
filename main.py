"""File contains a WordAnalyzer container providing various methods"""
from collections import Counter
from operator import itemgetter
from typing import List, Tuple


# ? Notes
# 1. Updated get_frequency_listed to account for alphabetical sorting
# 2. Added .lower() to force lower-case where needed.
# 3. Added __name__ line at bottom so output does not show when running tests
# 4. Added unnecessary variables to class (but commented out)
# 5. Skipped pseudo-interface as this serves no purpose for the task
# 6. The 're' module is still not needed. This is only counting & sorting.


class WordAnalyzer:
    """Provides methods to analyze a given text for occurances of words"""

    translator = str.maketrans({".": "", ",": ""})
    # words: str  # ! This never needs to be initialized
    # text: str  # ! We receive text, not words.
    # frequency: int  # ! This never needs to be initialized

    @staticmethod
    def max_frequency(text: str) -> int:
        """Returns the highest frequency of any word found in the text"""
        return max(
            Counter(
                text.lower().translate(WordAnalyzer.translator).split()
            ).most_common(1)
        )[1]

    @staticmethod
    def get_frequency(text: str, word: str) -> int:
        """Returns the frequency of the specified word in the text"""
        return Counter(text.lower().translate(WordAnalyzer.translator).split())[word]

    @staticmethod
    def get_frequency_listed(text: str, number: int) -> List[Tuple[str, int]]:
        """
        Returns a sorted list of {number} words ordered by frequency.
        In the case of words with the same frequency, they are returned
        alphabetically.
        """
        # ? Translate text
        text = text.lower().translate(WordAnalyzer.translator).split()

        # ? Count occurances & grab entries
        counter = Counter(text)
        entries = counter.most_common(len(counter))

        # ? Sort & reverse
        result = sorted(entries, key=itemgetter(1))
        result.reverse()

        return result[0:number]


# ! This shouldn't be necessary for conviniently outputting the results...
if __name__ == "__main__":
    with open("bacon.txt", "r") as file:
        text = file.read()
        print("max_frequency:", WordAnalyzer.max_frequency(text))
        print("get_frequency:", WordAnalyzer.get_frequency(text, "sirloin"))
        print(
            "get_frequency_listed:", WordAnalyzer.get_frequency_listed(text, 3)
        )
