import pytest
from random_script.random_script import LikeState, slap_many


# This decorator enables parametrization of arguments for a test function.
@pytest.mark.parametrize("test_input,expected", [
    ('ll', LikeState.empty),
    ('dd', LikeState.empty),
    ('ld', LikeState.disliked),
    ('dl', LikeState.liked),
    ('ldd', LikeState.empty),
    ('lldd', LikeState.empty),
    ('ddl', LikeState.liked),
])
def test_multi_slaps(test_input, expected):
    """
    Here, the @parametrize decorator defines three different (test_input,expected)
    tuples so that the test_eval function will run seven (7) times using them in turn.
    So it won't stop if any of the tests fails.
    """
    assert slap_many(LikeState.empty, test_input) is expected


# This decorator enables to skip a test function.
@pytest.mark.skip(reason="regexes not supported yet")
def test_regex_slaps():
    assert slap_many(LikeState.empty, '[ld]*ddl') is LikeState.liked


# This decorator enables not to count this test as a failure.
@pytest.mark.xfail
def test_divide_by_zero():
    assert 1 / 0 == 1


# Test if a specific exception is raised
def test_invalid_slap():
    with pytest.raises(ValueError):
        slap_many(LikeState.empty, 'x')


@pytest.mark.xfail
def test_db_slap(db_conn):  # Uses the db_slap fixture defined in conftest.py
    db_conn.read_slaps()
    assert ...


def test_print(capture_stdout):
    print("hello")
    assert capture_stdout["stdout"] == "hello\n"
