import random


def get_characters():
    alph_lower = [chr(i) for i in range(97, 123)]
    alph_upper = [chr(i) for i in range(65, 91)]
    nums = [str(i) for i in range(0, 10)]
    symbols_all = [chr(i) for i in range(33, 48)]

    return alph_lower, alph_upper, nums, symbols_all


def generate_password(length):
    alph_lower, alph_upper, nums, symbols_all = get_characters()
    all_characters = alph_lower + alph_upper + nums + symbols_all

    password = [random.choice(alph_lower), random.choice(alph_upper), random.choice(nums), random.choice(symbols_all)]
    password += random.choices(all_characters, k=length - 4)

    random.shuffle(password)
    return ''.join(password)


def main():
    while True:
        message = input('enter the length of your password: ')
        password_length = int(message)
        if password_length < 4:
            print('Password is too short.')
        else:
            print(f'Generated password: {generate_password(password_length)}')


if __name__ == "__main__":
    main()
