from loop_lab.textstats import char_count, line_count, word_count


def test_word_count_basic():
    assert word_count("hello world") == 2


def test_word_count_empty():
    assert word_count("") == 0


def test_word_count_apostrophes():
    assert word_count("don't stop") == 2


def test_char_count_with_whitespace():
    assert char_count("a b") == 3


def test_char_count_without_whitespace():
    assert char_count("a b\nc", include_whitespace=False) == 3


def test_line_count_empty():
    assert line_count("") == 0


def test_line_count_no_trailing_newline():
    assert line_count("one\ntwo") == 2


def test_line_count_trailing_newline():
    assert line_count("one\ntwo\n") == 2
