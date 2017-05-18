"""Tests for trigrams.py."""


import pytest


DICT_PARAMS = [
    ('and was', ['hot', 'shown']),
    ('he was', ['employing']),
    ('He was', ['pacing', 'at']),
    ('his hands', ['clasped'])
]

test_dict = {
    '1888--I was': ['returning'],
    'new problem.': ['I'],
    'see Holmes': ['again,'],
    'the blind.': ['He'],
    'had now': ['returned'],
    'his drug-created': ['dreams']
}


@pytest.mark.parametrize('word_pair, result_list', DICT_PARAMS)
def test_build_dict(word_pair, result_list):
    """Test the build_dict function."""
    from trigrams import build_dict
    assert build_dict()[word_pair] == result_list


def test_get_random():
    """Test the get_random function."""
    from trigrams import get_random
    for n in range(1, 100):
        assert get_random(n) in range(n)


def test_build_words():
    """Test the build_words function."""
    from trigrams import build_words
    for n in range(10, 100):
        assert len(build_words(n, test_dict).split()) == n
