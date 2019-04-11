import re
import sys
import os


def load_bad_passwords(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, encoding='utf-8') as file:
        return file.read().split()


def has_good_len(password):
    if len(password) > 16:
        return 4
    elif len(password) > 12:
        return 3
    elif len(password) > 8:
        return 2
    elif len(password) > 4:
        return 1
    return 0


def has_upper_and_lower(password):
    return not password.isupper() ^ password.islower()


def has_dates_or_phone_numbers(password):
    if re.search(r'\d{4}', password):
        return 0
    else:
        return 1


def has_special_symbols(password):
    if re.search('[\W_]', password):
        return 1
    else:
        return 0


def check_bad_passwords(password):
    if len(sys.argv) > 1:
        path = sys.argv[1]
        bad_passwords = load_bad_passwords(path)
    else:
        return 0
    if bad_passwords:
        if password in bad_passwords:
            return 0
        else:
            return 1


def has_digits(password):
    if re.search('[\d]', password):
        print('has_digit')
        return 1
    else:
        return 0


def get_password_strength(password):
    password_str = 1
    checking_functions = [
        has_special_symbols,
        has_good_len,
        has_upper_and_lower,
        has_dates_or_phone_numbers,
        has_digits,
        check_bad_passwords,
    ]
    for func in checking_functions:
        password_str += func(password)
    return password_str


if __name__ == '__main__':
    print('Введите пароль')
    password = input().split()[0]
    password_strength = get_password_strength(password)
    print(password_strength)
