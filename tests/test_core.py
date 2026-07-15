from text_tools.core import word_count, reverse_words, capitalize_each, char_count

def test_word_count_basic():
    assert word_count("hello brave new world") == 4 # deliberately wrong


def test_word_count_empty():
    assert word_count("") == 0


def test_reverse_words():
    assert reverse_words("one two three") == "three two one"


def test_capitalize_each():
    assert capitalize_each("hello there world") == "Hello There World"

def test_char_count_with_spaces():
    assert char_count("ab cd") == 5

def test_char_count_without_spaces():
    assert char_count("ab cd", include_spaces=False) == 4
