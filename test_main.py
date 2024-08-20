from main import greet_user

def test_greet_user():
    assert greet_user("Alice") == "Hello, Alice!", f"Expected 'Hello, Alice!', but got {greet_user('Alice')}"
    assert greet_user("Bob") == "Hello, Bob!", f"Expected 'Hello, Bob!', but got {greet_user('Bob')}"
    assert greet_user("") == "Hello, !", f"Expected 'Hello, !', but got {greet_user('')}"
