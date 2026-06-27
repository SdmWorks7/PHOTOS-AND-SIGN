from hello import get_user_email

def test_normal_list(users: str):
    assert get_user_email(users, "saumya") == "saumya@gmail.com"

def test_empty_list(users: str):
    assert get_user_email(users, " ") == None
