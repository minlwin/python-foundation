from src.hello import say_hello

def test_say_hello():
    assert say_hello("Python") == "Hello Python"