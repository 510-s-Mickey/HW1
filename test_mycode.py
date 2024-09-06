# test_mycode.py
from mycode import add

def test_add_pass():
    assert add(2, 3) == 5  # this test should succeed

# If we uncomment the test_add_fail function, the workflow test will fail.
def test_add_fail():
    assert add(2, 5) == 5  # this test should fail


