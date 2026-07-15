from text_tools.core import word_count, reverse_words, capitalize_each


def test_word_count_basic():
    assert word_count("hello brave new world") == 4


def test_word_count_empty():
    assert word_count("") == 0


def test_reverse_words():
    assert reverse_words("one two three") == "three two one"


def test_capitalize_each():
    assert capitalize_each("hello there world") == "Hello There World"