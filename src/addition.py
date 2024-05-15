# app.py
# This is a test commit
def add(a, b):
    return a - b

def test_add():
    assert add(1, 2) == -1
    assert add(1, -1) == 2
