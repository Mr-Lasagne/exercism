"""Solution to Little Sister's Essay."""


def capitalize_title(title: str) -> str:
    """Convert the given string to title case.

    :param title: Title string that needs converting to title case.
    :type title: str
    :return: Title string in title case.
    :rtype: str
    """
    return title.title()


def check_sentence_ending(sentence: str) -> bool:
    """Check the ending of the sentence to verify that a period is present.

    :param sentence: A sentence to be checked for an ending period.
    :type sentence: str
    :return: True if punctuated correctly with a period, False otherwise.
    :rtype: bool
    """
    return sentence.endswith(".")


def clean_up_spacing(sentence: str) -> str:
    """Remove any leading and trailing whitespace from a sentence.

    :param sentence: A sentence to clean of leading and trailing whitespace.
    :type sentence: str
    :return: A sentence that has had leading and trailing whitespace removed.
    :rtype: str
    """
    return sentence.strip()


def replace_word_choice(sentence: str, old_word: str, new_word: str) -> str:
    """Replace a word in the provided sentence with a new one.

    :param sentence: A sentence containing a word to be replaced.
    :type sentence: str
    :param old_word: The word to replace.
    :type old_word: str
    :param new_word: The replacement word.
    :type new_word: str
    :return: The input sentence with the new word in place of the old word.
    :rtype: str
    """
    return sentence.replace(old_word, new_word)
