"""Tests for trigrams.py."""


import pytest


DICT_PARAMS = [
    ('and was', ['hot', 'shown']),
    ('he was', ['employing']),
    ('He was', ['at', 'pacing']),
    ('his hands', ['clasped'])
]


@pytest.mark.parametrize('word_pair, result_list', DICT_PARAMS)
def test_build_dict(word_pair, result_list):
    """."""
    from trigrams import build_dict
    from trigrams import dictionary
    build_dict()
    assert dictionary[word_pair] == result_list


@pytest.mark.parametrize('word_pair, result_list', DICT_PARAMS)
def test_build_words(word_pair, result_list):
    """."""
    from trigrams import choose_third
    assert choose_third(word_pair) in result_list
