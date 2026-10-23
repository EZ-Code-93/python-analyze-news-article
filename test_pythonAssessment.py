import pytest
from pythonAssessment import (
    count_specific_word,
    identify_most_common_word,
    calculate_average_word_length,
    count_paragraphs,
    count_sentences
)

# ==========================================
# Tests for count_specific_word(str, str)
# ==========================================

def test_count_specific_word_normal():
    text = "The quick brown fox jumps over the lazy dog."
    assert count_specific_word(text, "the") == 2
    assert count_specific_word(text, "fox") == 1

def test_count_specific_word_no_matches_edge_case():
    text = "The quick brown fox jumps over the lazy dog."
    assert count_specific_word(text, "cat") == 0

def test_count_specific_word_empty_string():
    assert count_specific_word("", "the") == 0


# ==========================================
# Tests for identify_most_common_word(str)
# ==========================================

def test_identify_most_common_word_normal():
    text = "apple banana apple orange banana apple"
    result = identify_most_common_word(text)
    assert result == "apple"

def test_identify_most_common_word_empty_edge_case():
    assert identify_most_common_word("") is None
    assert identify_most_common_word("   ") is None


# ==========================================
# Tests for calculate_average_word_length(str)
# ==========================================

def test_calculate_average_word_length_normal():
    assert calculate_average_word_length("the cat") == 3.0

def test_calculate_average_word_length_empty_edge_case():
    assert calculate_average_word_length("") == 0
    assert calculate_average_word_length("   ") == 0


# ==========================================
# Tests for count_paragraphs(str)
# ==========================================

def test_count_paragraphs_normal():
    text = "This is paragraph one.\n\nThis is paragraph two."
    assert count_paragraphs(text) == 2

def test_count_paragraphs_empty_edge_case():
    assert count_paragraphs("") == 1
    assert count_paragraphs("   ") == 1


# ==========================================
# Tests for count_sentences(str)
# ==========================================

def test_count_sentences_normal():
    text = "Hello world! This is a test. Is it working?"
    assert count_sentences(text) == 3

def test_count_sentences_empty_edge_case():
    assert count_sentences("") == 1
    assert count_sentences("   ") == 1
