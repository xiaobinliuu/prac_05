def main():
    name_to_email = {}
    user_email = input("Enter your email: ")
    while user_email != "":
        user_name = separate_name(user_email)
        check_name = input(f"Is your name {user_name}(Y/n)").upper()
        if check_name != "" and check_name != "Y":
            user_name = input("Enter your name: ")
        name_to_email[user_name] = user_email
        user_email = input("Enter your mail: ")
        for key, value in name_to_email.items():
            print(f"{key} ({value})")


def separate_name(user_email):
    name = user_email.split('@')[0]
    split_name = name.split('.')
    user_name = ".".join(split_name).title()
    return user_name


main()
