"""Unit tests for dictionary functions"""

__author__ = "730824316"

from exercises.ex03.dictionary import invert, count, favorite_color, bin_len


def test_invert_use_case() -> None:
    """Test the invert function"""
    assert invert(my_dictionary={"apple": "cat"}) == {"cat": "apple"}


def test_invert_use_case_2() -> None:
    """Test the invert function"""
    assert invert(my_dictionary={"a": "z", "b": "y", "c": "x"}) == {
        "z": "a",
        "y": "b",
        "x": "c",
    }


def test_invert_edge_case() -> None:
    """Test the invert function for unexpected input"""
    assert invert(my_dictionary={}) == {}


def test_count_use_case() -> None:
    """Test the count function given expected inputs"""
    assert count(given_list=["red", "yellow", "blue", "blue", "blue"]) == {
        "red": 1,
        "yellow": 1,
        "blue": 3,
    }


def test_count_use_case_2() -> None:
    """Test the count function given expected inputs"""
    assert count(given_list=["red", "yellow", "blue"]) == {
        "red": 1,
        "yellow": 1,
        "blue": 1,
    }


def test_count_edge_case() -> None:
    """Test the count function behavior for unexpected input"""
    assert count(given_list=[""]) == {"": 1}


def test_favorite_color_use_case() -> None:
    """Test the favorite_color function given an expected input"""
    assert (
        favorite_color(favcol={"Shriya": "green", "Robin": "green", "Saachi": "yellow"})
        == "green"
    )


def test_favorite_color_use_case_2() -> None:
    """Test the favorite_color function given a tie of popular colors"""
    assert (
        favorite_color(
            favcol={
                "Shriya": "green",
                "Robin": "green",
                "Saachi": "yellow",
                "Anna": "yellow",
            }
        )
        == "green"
    )


def test_favorite_color_edge_case() -> None:
    """Test the favorite color function with an unexpected input"""
    assert favorite_color(favcol={}) == ""


def test_bin_len_use_case() -> None:
    """Test the bin_len function given an expected input"""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_use_case_2() -> None:
    """Test the bin_len function given an expected input"""
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len_edge_case() -> None:
    """Test the bin_len function given an unexpected input"""
    assert bin_len([]) == {}
