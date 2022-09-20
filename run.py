""" App file """
import sys
import time
import gspread
from google.oauth2.service_account import Credentials
import ascii_img
import lines_and_stories


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("pp3-python")

name = ""


def slow_type(data):
    """ Slow down the print time for one line, taken from tutorial,
    credit in README
    """
    for character in data:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(.05)
    return ""


def welcome():
    """
    Display the welcome message
    """
    print(f"\033[1;31;48m{ascii_img.WELCOME}")
    slow_type(f"\033[1;31;48m{lines_and_stories.WELC_LINE} \n")
    slow_type("Only rule here is that you need to answer my questions \n"
              "where you see =>, so I can continue.\n")


def get_name():
    """
    Collect the user's name and validate it to no be empty
    """
    global name
    slow_type("\n"
              "Now tell me your name ...\n")
    name = input("=> ").strip()
    if name != "":
        time.sleep(1)
        slow_type("\n"
                  f"{name}, that name, it reminds me of a story...\n")
        age()
    else:
        slow_type("You are not following the rules...\n")
        get_name()


def age():
    """
    Get user's age and validate it. Calls the next step to follow
    if under 10, gives it a message and exit, if 100 and over gives
    a message and ask for a valid one
    Modified accorder to suggestions and guidance of my mentor Brian Macharia
    """
    slow_type("but first, tell me your age...\n")
    while True:
        age_input = input("=> ").strip()
        if not age_input.isdigit():
            slow_type("You are not following the rules."
                      " You must enter a number.\n")
            continue
        if int(age) > 99:
            slow_type("You not following the rules."
                      "You must enter a number less than 100.\n")
            continue
        if int(age) < 10:
            slow_type("Oh you are too young yet, sorry"
                      " I may offer you in a next time a lullaby...\n")
            slow_type(ascii_img.BABY)
            slow_type("Bye for now...")
            sys.exit()
        else:
            slow_type("\n"
                      "ok, you are old enough but are you brave enough?\n")
            slow_type("\n"
                      "Do you want to continue? 'y' for yes or 'n' for no \n")
            answer = input("=> ")
            if answer == "n":
                slow_type("\n"
                          "So you chicken out?\n"
                          "I did not expect that from you.\n")
                print(ascii_img.CHICKEN)
                sys.exit()
            else:
                slow_type("\n"
                          "Seems I meet a brave one, let's start...\n")
                clear()
                pick_story()


def pick_story():
    """ Allows the user to pick the main direction of the story,
    choosing between 3 options
    """
    print(f"\033[1;31;48m {ascii_img.HOUSE}\n")
    slow_type(f"{lines_and_stories.intro}\n"
              f"{name} {lines_and_stories.intro1}\n"
              f"{lines_and_stories.intro2}\n")
    clear()
    slow_type(f"\033[1;31;48mTell me what do you think {name} will do"
              " now that is at home?\n")
    slow_type("\n"
              " 1. Draw.\n 2. Do homework.\n 3. Take a nap.\n")
    stor_pick = input("\n""=> ")
    picked = ""
    if int(stor_pick) == 1:
        picked = lines_and_stories.story_picked[0]
        print(f"\033[1;31;48m{ascii_img.DOING_ART}")
        slow_type(f"You were right, {name} headed to {picked},"
                  " so went to the studio.\n")
        story_draw()
    elif int(stor_pick) == 2:
        picked = lines_and_stories.story_picked[1]
        slow_type(f"Yes, {name} headed to {picked}, so went to desk.\n")
        story_kitchen()
    elif int(stor_pick) == 3:
        picked = lines_and_stories.story_picked[2]
        slow_type(f"Picked right there, {name} headed to {picked},"
                  " so went to the second floor.\n")
        story_closet()
    else:
        slow_type("You had not pick a valid option, try again...\n")
        pick_story()


def story_draw():
    """
    Runs the option for the drawing story
    """
    draw_pick = ""
    street_pick = ""
    clear()
    slow_type(f"\033[1;31;48mEvery since was young {name} always"
              " had a power that\n"
              "had kept secret... whatever drew came true!\n"
              "\nEvery day have played with Elizabeth, the best friend\n"
              " anyone could have, they would play on magical creations that\n"
              f" came straight from {name}'s imagination, in castles, etc\n")
    print(ascii_img.PRINCESS)
    slow_type(f"But as them got older, they grew apart.\n"
              f"{name} threw herself deeper into painting \n"
              "while Elizabeth played sports and started hanging out\n"
              "with other friend Jessica more often\n")
    print(ascii_img.BASKETBALL)
    clear()
    slow_type("However, the two still maintained a tradition of meeting\n"
              "in front of school and walking home together until one day...\n"
              f"{name} was waiting for long time outside for Elizabeth,\n"
              "but she still did not come.\n"
              "\n")
    clear()
    slow_type(f"\033[1;35;40mWhat should I do?"f"Though {name}\n")
    slow_type("\n1. Go home.\n2. Go looking for Elizabeth.\n3. Go back into"
              " the school again and ask for more homework.\n")
    draw_pick = input("\n""=> ")
    if int(draw_pick) == 1:
        slow_type("\n"f"{name} then went home, was enrange thinking that"
                  " Elizabeth\n"
                  "let her down. And passed the afternoon in bed upset.\n")
        at_school_next_day()
    elif int(draw_pick) == 2:
        slow_type("\n"f"So {name} went looking for Elizabeth and walk\n"
                  " and walk... until got in a strange street\n"
                  "that never had been in before, suddenly ..."
                  " she was lost!\n")
        slow_type(f"What now... {name} though\n"
                  "\n1. Yell for help?\n2. Keep walking.\n")
        street_pick = input("\n""=> ")
        if int(street_pick) == 1:
            slow_type(f"So {name} did, and a lady respond and help"
                      " so could make it back home\n")
            at_school_next_day()
        elif int(street_pick) == 2:
            slow_type("\nSo that was the last time someone knew of \n"
                      f"{name},only thing that was left were the draws...\n")
            print(ascii_img.end_banner)
            time.sleep(1)
            exit()
        else:
            slow_type("That's not a valid option. Try again...\n")
    elif int(draw_pick) == 3:
        slow_type("\n"f"{name} went then into the school and"
                  " dedicate her time to homework.\n"
                  "Never again draw or talk to anybody else.")
        clear()
        exit_app()
    else:
        slow_type("\n""You had not pick a valid option, try again...\n")
        pick_story()


def at_school_next_day():
    """
    Display next part of the story draw
    """
    clear()
    print("at school next day")
    slow_type("And then it happened again the next day.\n"
              "After days and days of Elizabeth no showing up,\n"
              "Sarah confronted her at school")
    slow_type(f"\033[1;36;40mWhy won't you walk home with me?"
              "she asked")
    slow_type(f"\033[1;32;40mI walk home with Jessica now."
              "said Elizabeth\n It’s no big deal Sometimes things change.\n"
              f"\033[1;35;40m {name}{lines_and_stories.hola}")


def story_kitchen():
    """
    Starts the kitchen story option
    """
    print("kitchen")


def story_closet():
    """
    Open the flow to the closet story
    """
    print("closet")


def clear():
    """
    Clears the screen for the next content to be display
    taken from RickofManc/vv-pizzas
    """
    print("\033c")


def exit_app():
    """
    Display the end banner, and exit the app after a second
    """
    slow_type(ascii_img.END_BANNER)
    time.sleep(1)
    sys.exit()


welcome()
get_name()
