def get_int_input(display_text="Int: "):
    while True:
        raw_user_input = input(display_text)

        if raw_user_input == "":
            exit()
        elif raw_user_input.isnumeric():
            return int(raw_user_input)
        else:
            print("Invalid input. Please enter a number. (Blank to exit)")

def get_bool_yes_no_input():
    return input("(Y/N): ").upper() == "Y"


def get_striped_string_input(display_text):
    return input(display_text).strip()
