import random
import string
import os
from rich.console import Console
console = Console()

def generate_personal_password(name, age, length=12, use_uppercase=False, use_special_chars=False, model=None):
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")
    
    if model == 'complex':
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    base = f"{name.lower()}{age}"
    if use_uppercase:
        base = base.title()

    if len(base) >= length:
        return base[:length]

    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation

    base += ''.join(random.choices(characters, k=length - len(base)))
    return ''.join(random.sample(base, len(base)))

def generate_remote_desktop_password(length=16, use_uppercase=False, use_special_chars=True, model=None):
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")
    
    if model == 'complex':
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    characters = string.ascii_letters + string.digits
    if use_uppercase:
        characters = characters.upper() + characters
    if use_special_chars:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

def generate_username(name, prefix='', suffix='', length=15, model=None):
    if model == 'simple':
        base_username = f"{prefix}{name.lower().replace(' ', '_')}{suffix}"
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    
    username = f"{prefix}{name.lower().replace(' ', '_')}{suffix}"
    return username[:length]

def generate_wordlist(num_words, length=8, special_chars=False, use_uppercase=False, model=None):
    if model == 'complex':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits
    
    if special_chars:
        characters += string.punctuation
    if use_uppercase:
        characters = characters.upper() + characters

    words = [''.join(random.choice(characters) for _ in range(length)) for _ in range(num_words)]
    return words

def generate_keyword_based_passwords(keywords, num_passwords=50, length=12, use_special_chars=False, use_uppercase=False):
    passwords = []
    for keyword in keywords:
        keyword = keyword.lower().replace(" ", "_")
        while len(passwords) < num_passwords:
            password = keyword + ''.join(random.choices(string.ascii_letters + string.digits, k=length - len(keyword)))
            if use_special_chars:
                password += ''.join(random.choices(string.punctuation, k=1))
            if use_uppercase:
                password = password.upper()
            password = ''.join(random.sample(password, len(password)))
            passwords.append(password)
            if len(passwords) >= num_passwords:
                break
    return passwords

def common_usernames(name, num=50, prefix='', suffix=''):
    base_username = f"{prefix}{name.lower().replace(' ', '_')}{suffix}"[:15]
    common_suffixes = [
        '123', 'abc', 'user', 'admin', '2024', 'guest', 'test', 'admin1', 'welcome', 'password',
        '2023', '2025', 'admin2', 'qwerty', 'password1', 'letmein', 'welcome1', 'welcome2', 
        'letmein123', 'pass123', 'hello123', '1234', 'love', 'iloveyou', 'sunshine', 'sunny',
        'moonlight', 'star', 'admin123', '12345', '654321', 'iloveyou1', 'qwerty123', '123qwe',
        'password123', 'qwertyui', '1q2w3e4r', 'zxcvbnm', 'asdfghjkl', 'qazwsx', 'mypass', 
        'mypassword', 'yourpassword', 'myname', 'myname123', 'random', 'password1', 'hello', 
        'mypass123', 'welcome123', 'qwe123', 'asdf123', 'zxc123', 'password2024', 'abc123'
    ]
    return [f"{base_username}{suffix}"[:15] for suffix in common_suffixes[:num]]

def country_based_wordlist(country, num_words=50, length=8):
    base_word = country.lower().replace(" ", "_")
    words = [f"{base_word}_{i+1}"[:length] for i in range(num_words)]
    return words

def keyword_based_wordlist(keywords, num_words=50, length=8):
    words = []
    for keyword in keywords:
        keyword = keyword.lower().replace(" ", "_")
        for i in range(num_words // len(keywords)):
            words.append(f"{keyword}_{i+1}"[:
length])
    return words

def append_to_file(filename, data):
    try:
        with open(filename, 'a') as f:
            for item in data:
                f.write(f"{item}\n")
    except IOError as e:
        print(f"Error writing to file: {e}")

def validate_positive_integer(value, name):
    try:
        int_value = int(value)
        if int_value <= 0:
            raise ValueError(f"{name} must be positive.")
        return int_value
    except ValueError as e:
        print(f"Invalid input for {name}: {e}")
        return None

def main():
    listmaker = """
██╗     ██╗███████╗████████╗    ███╗   ███╗ █████╗ ███████╗██████╗ 
██║     ██║██╔════╝╚══██╔══╝    ████╗ ████║██╔══██╗██╔════╝██╔══██╗
██║     ██║███████╗   ██║       ██╔████╔██║███████║█████╗  ██████╔╝
██║     ██║╚════██║   ██║       ██║╚██╔╝██║██╔══██║██╔══╝  ██╔══██╗
███████╗██║███████║   ██║       ██║ ╚═╝ ██║██║  ██║███████╗██║  ██║
╚══════╝╚═╝╚══════╝   ╚═╝       ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                                                                                                                                        
    """
    creator = "Created by Cipher security"
    channel = "Telegram: @Cipher_security"
    github = "github: Cipher1security"
    console.print(listmaker, style="bold blue")
    console.print(creator, style="bold green")
    console.print(channel, style="bold green")
    console.print(github, style="bold green")
    
    print("list maker - The creator of password list and half list user")
    print("1. Generate Password List")
    print("2. Generate VPS Wordlist")
    choice = input("Select an option (1/2): ")

    if choice == '1':
        name = input("Enter your name: ")
        age = input("Enter your age: ")

        num_passwords = validate_positive_integer(input("How many personal passwords do you want to generate? "), "Number of passwords")
        
        while True:
            password_length = validate_positive_integer(input("Enter the length of each personal password (minimum 8): "), "Password length")
            if password_length is not None and password_length >= 8:
                break
            print("Password length must be at least 8 characters. Please try again.")

        print("Do you want to include uppercase letters in the password? (yes/no)")
        use_uppercase = input().strip().lower() == 'yes'
        print("Do you want to include special characters in the password? (yes/no)")
        use_special_chars = input().strip().lower() == 'yes'
        print("Do you want to use a complex model for passwords? (yes/no)")
        model = input().strip().lower()
        if model == 'yes':
            model = 'complex'
        else:
            model = None

        personal_passwords = [generate_personal_password(name, age, password_length, use_uppercase, use_special_chars, model) for _ in range(num_passwords)]

        print("Do you want to include special character combinations in the password list? (yes/no)")
        if input().strip().lower() == 'yes':
            additional_words = generate_wordlist(50, length=password_length, special_chars=use_special_chars, use_uppercase=use_uppercase, model=model)
            personal_passwords.extend(additional_words)

            print("Do you want to include country-based words in the password list? (yes/no)")
            if input().strip().lower() == 'yes':
                country = input("Enter a country name: ")
                country_words = country_based_wordlist(country, num_words=50, length=password_length)
                personal_passwords.extend(country_words)
        
        append_to_file('personal_passwords.txt', personal_passwords)
        print(f"Personal passwords appended to 'personal_passwords.txt'")

    elif choice == '2':
        print("1. Generate VPS Username List")
        print("2. Generate VPS Password List")
        sub_choice = input("Select an option (1/2): ")

        if sub_choice == '1':
            num_usernames = validate_positive_integer(input("How many usernames do you want to generate? "), "Number of usernames")
            name = input("Enter a base name for usernames: ")

            if num_usernames is None:
                return

            print("Do you want to include a prefix for usernames? (yes/no)")
            prefix = input("Enter prefix: ") if input().strip().lower() == 'yes' else ''
            print("Do you want to include a suffix for usernames? (yes/no)")
            suffix = input("Enter suffix: ") if input().strip().lower() == 'yes' else ''
            print("Do you want to use a simple model for usernames? (yes/no)")
            model = input().strip().lower()
            if model == 'yes':
                model = 'simple'
            else:
                model = None

            usernames = [generate_username(name + str(i), prefix, suffix, length=15, model=model) for i in range(num_usernames)]

            print("Do you want to include common usernames in the username list? (yes/no)")
            if input().strip().lower() == 'yes':
                additional_usernames = common_usernames(name, num=num_usernames, suffix=suffix, prefix=prefix)
                usernames.extend(additional_usernames)

            print("Do you want to include country-based usernames in the username list? (yes/no)")
            if input().strip().lower() == 'yes':
                country = input("Enter a country name: ")
                country_usernames = country_based_wordlist(country, num_words=num_usernames, length=15)
                usernames.extend(country_usernames)
            
            append_to_file('remote_desktop_usernames.txt', usernames)
            print(f"Remote desktop usernames appended to 'remote_desktop_usernames.txt'")

        elif sub_choice == '2':
            num_passwords = validate_positive_integer(input("How many passwords do you want to generate? "), "Number of passwords")
            password_length = validate_positive_integer(input("Enter the length of each password: "), "Password length")

            if num_passwords is None or password_length is None:
                return

            print("Do you want to include uppercase letters in the password? (yes/no)")
            use_uppercase = input().strip().lower() == 'yes'
            print("Do you want to include special characters in the password? (yes/no)")
            use_special_chars = input().strip().lower() == 'yes'
            print("Do you want to use a complex model for passwords? (yes/no)")
            model = input().strip().lower()
            if model == 'yes':
                model = 'complex'
            else:
                model = None

            remote_desktop_passwords = [generate_remote_desktop_password(password_length, use_uppercase, use_special_chars, model) for _ in range(num_passwords)]

            print("Do you want to include special character combinations in the password list? (yes/no)")
            if input().strip().lower() == 'yes':
                additional_words = generate_wordlist(50, length=password_length, special_chars=use_special_chars, use_uppercase=use_uppercase, model=model)
                remote_desktop_passwords.extend(additional_words)

                print("Do you want to include country-based words in the password list? (yes/no)")
                if input().strip().lower() == 'yes':
                    country = input("Enter a country name: ")
                    country_words = country_based_wordlist(country, num_words=50, length=password_length)
                    remote_desktop_passwords.extend(country_words)
            
            print("Do you want to include keyword-based words in the password list? (yes/no)")
            if input().strip().lower() == 'yes':
                keywords = [input(f"Enter keyword {i+1}: ") for i in range(8)]
                keyword_passwords = generate_keyword_based_passwords(keywords, num_passwords=num_passwords, length=password_length, use_special_chars=use_special_chars, use_uppercase=use_uppercase)
                remote_desktop_passwords.extend(keyword_passwords)
            
            append_to_file('remote_desktop_passwords.txt', remote_desktop_passwords)
            print(f"Remote desktop passwords appended to 'remote_desktop_passwords.txt'")

        else:
            print("Invalid choice")

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
