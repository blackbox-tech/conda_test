import conda_test

def test_import():
    assert conda_test.message() == "hello"