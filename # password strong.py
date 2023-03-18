# password strong
def is_acceptable_password(password: str) -> bool:
    # my code here
    return len(password) > 6 and not all(i.isdigit() for i in password)and not all(i.isalpha() for i in password)


print(is_acceptable_password("Thisisádf sfasfasf"))