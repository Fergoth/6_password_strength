import re
import sys
import os
import getpass


def load_bad_passwords(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, encoding='utf-8') as file:
        return file.read().splitlines()


def has_good_len(password):
    best_quality = 4
    len_quality = [
        (4, 0),
        (8, 1),
        (12, 2),
        (16, 3),
    ]
    for length, quality in len_quality:
        if len(password) < length:
            return quality
    return best_quality


def has_upper_and_lower(password):
    return not password.isupper() ^ password.islower()


def has_dates_or_phone_numbers(password):
    return not bool(re.search(r'\d{4}', password))


def has_special_symbols(password):
    return bool(re.search('[\W_]', password))


def get_bad_passwords_from_file():
    if len(sys.argv) > 1:
        path = sys.argv[1]
        return load_bad_passwords(path)


def check_bad_passwords(password):
    bad_passwords = get_bad_passwords_from_file()
    if bad_passwords:
        if password in bad_passwords:
            return 0
        else:
            return 1


def has_digits(password):
    return bool(re.search('[\d]', password))


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
    password = getpass.getpass()
    password_strength = get_password_strength(password)
    print(password_strength)
