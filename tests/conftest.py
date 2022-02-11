import pytest
import sys

"""
test functions request fixtures they require by declaring them as arguments
When pytest goes to run a test, it looks at the parameters in that test function’s signature,
and then searches for fixtures that have the same names as those parameters. 
Once pytest finds them, it runs those fixtures, captures what they returned (if anything), 
and passes those objects into the test function as arguments.

In this case, this is its own module so it can be reachable from anywhere. 
"""


@pytest.fixture
def capture_stdout(monkeypatch):
    buffer = {"stdout": "", "write_calls": 0}

    def fake_write(s):
        buffer["stdout"] += s
        buffer["write_calls"] += 1

    monkeypatch.setattr(sys.stdout, 'write', fake_write)
    return buffer


@pytest.fixture(scope="session")  # The scope of the fixture will allow to call this just once for all tests
def db_conn():
    db = ...
    url = ...
    with db.connect(url) as conn:  # connection will be torn down after all tests finish
        yield conn