#!/usr/bin/env python3

from colorama import Fore, Style
from simple_term_menu import TerminalMenu

def exit_app():
    clear()
    print('You Exited SuccessFully')
    exit()
def clear():

    import os
    os.system('clear')
def soon():
    clear()
    print("this feature will be added soon ...")
    main()
def Base64_Menu():
    text_options = [
        "[1] Base64 to Text",
        "[2] Text to Base64",
        "[3] Back to text menu"
        ]
    text_title = 'Welcome to pytool app select everything you want'
    terminal_menu = TerminalMenu(text_options, title=text_title)
    menu_entry_index = terminal_menu.show()
    selected = menu_entry_index
    if(selected == 0): base64_to_string()
    if(selected == 1): string_to_base64()
    elif(selected == 2): text_menu()
    else:
        soon()
def text_menu():
    text_options = [
        "[1] Base64",
        "[2] soon",
        "[3] soon",
        "[4] soon",
        "[5] soon",
        "[6] soon",
        "[7] soon",
        "[8] more",
        "[9] main menu"
        ]
    text_title = 'Welcome to pytool app select everything you want'
    terminal_menu = TerminalMenu(text_options, title=text_title)
    menu_entry_index = terminal_menu.show()
    selected = menu_entry_index
    if(selected == 0): Base64_Menu()
    elif(selected == 8): main()
    else:
        soon()
def base64_to_string():
    text = input("Input you're base64 text => ").encode()
    clear()
    if(text != ''):
        test = check_base64(text)
        if(test == True):
            import base64
            with open('text.txt', 'w') as f:
                f.write(base64.b64decode(text).decode('utf-8'))
            print(f"{Fore.GREEN}You're Base64 decoded successfully you can find string in text.txt file{Style.RESET_ALL}")
        else:
            print('text is not base64')
    else:
        print('text is empty')
    main()
def string_to_base64():
    text = input("Input you're text => ").encode()
    clear()
    import base64
    base64encoded = base64.b64encode(text)
    with open('base64.txt', 'w') as f:
        f.write(base64encoded.decode('utf-8'))
    print(f"""{Fore.GREEN}You're text encoded successfully 
    Base64 => {base64encoded.decode('utf-8')}
    Also you can find base64 in base64.txt file{Style.RESET_ALL}""")
    main()
def check_base64(text):
    import base64, binascii
    try:
        base64.b64decode(text, validate=True)
    except binascii.Error:
        return False
    return True

def main():
    main_options = ["[1] Text", "[2] soon", "[3] soon", "[4] soon", "[5] soon", "[6] soon", "[7] soon", "[8] soon", "[9] exit"]
    main_title = 'Welcome to pytool app select everything you want'
    terminal_menu = TerminalMenu(main_options, title=main_title)
    menu_entry_index = terminal_menu.show()
    selected = menu_entry_index
    if(selected == 0): text_menu()
    elif(selected == 8): exit_app()
    else:
        soon()

if __name__ == "__main__":
    clear()
    main()
