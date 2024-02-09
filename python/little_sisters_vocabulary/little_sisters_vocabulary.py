"""Solution to Little Sister's Vocabulary."""

from __future__ import annotations

import string


def add_prefix_un(word: str) -> str:
    """Add the 'un' prefix to the word.

    :param word: The given word.
    :type word: str
    :return: The given word prepended with 'un'.
    :rtype: str
    """
    return "un" + word


def make_word_groups(vocabulary_words: list[str]) -> str:
    """Prepend a prefix to a list of words and connect the new words.

    :param vocabulary_words: A list of words with the prefix in first index.
    :type vocabulary_words: list[str]
    :return: The prefix followed by each word with the prefix prepended.
    :rtype: str
    """
    return (" :: " + vocabulary_words[0]).join(vocabulary_words)


def remove_suffix_ness(word: str) -> str:
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: The word to remove the suffix from.
    :type word: str
    :return: The word with the suffix removed with the spelling adjusted as
        necessary.
    :rtype: str
    """
    if word.endswith("iness"):
        return word[:-5] + "y"
    return word.removesuffix("ness")


def adjective_to_verb(sentence: str, index: int) -> str:
    """Change the adjective within the sentence to a verb.

    :param sentence: The sentence containing the word.
    :type sentence: str
    :param index: The index of the word to remove and transform.
    :type index: int
    :return: The extracted adjective changed to a verb.
    :rtype: str
    """
    return sentence.split()[index].strip(string.punctuation) + "en"
