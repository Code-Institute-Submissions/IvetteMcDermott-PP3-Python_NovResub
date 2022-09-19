import gspread
from google.oauth2.service_account import Credentials
import ascii_img
import lines_and_stories
import sys
import time



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


def slowType(data):
    """ Slow down the print time for one line, taken from tutorial,
    credit in README """

    for character in data:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(.1)
    return ""


def slowTypeF(data):
    """ Slow down the print time but continue, for long texts, taken from 
    tutorial, credit in README """

    for character in data:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(.03)
    return ""


def slowTypeDif(data):
    """ Slow down the print time with 2 sets of time, taken from 
    tutorial, credit in README """

    for character in data:
        sys.stdout.write(character)
        sys.stdout.flush()
        if character != "\n":
            time.sleep(.1)
        else:
            time.sleep(1)
    return ""


def welcome():
    """ Display the welcome message """
    print(f"\033[1;31;48m{ascii_img.welcome}")
    slowType(f"\033[1;31;48m{lines_and_stories.WELC_LINE} \n")
    slowType("Only rule here is that you need to answer my questions \n"
    "where you see =>, so I can continue.\n")


def get_name():
    global name
    """ Collect the user"s name and validate it to no be empty """
    slowType("\n"
        "Now tell me your name ...\n")
    name = input("=> ").strip()
    if name != "":
        time.sleep(1)
        slowType("\n"
            f"{name}, that name, it reminds me of a story...\n")
        age()
    else:
        slowType("You are not following the rules...\n")
        get_name()


def age():
    """ Get user's age and validate it. Calls the next step to follow
        if under 10, gives it a message and exit, if 100 and over gives
        a message and ask for a valid one
        Modified accorder to suggestions and guidance of my mentor Brian Macharia
    """
    global name
    slowType(f"but first, tell me your age...\n")
    
    while True:
        age_input = input("=> ").strip()
        if not age_input.isdigit():
            slowType("You are not following the rules."
            " You must enter a number.\n")
            continue
        age = int(age_input)
        if age > 99:
            slowType("You not following the rules."
            "You must enter a number less than 100.\n")
            continue
        if age < 10:
            slowType("Oh you are too young yet, sorry"
            " I may offer you in a next time a lullaby...\n")
            slowType(ascii_img.baby)
            slowType("Bye for now...")
            sys.exit()
        else:
            slowType("\n"
            "ok, you are old enough but are you brave enough?\n")
            slowType("\n"
                "Do you want to continue? 'y' for yes or 'n' for no \n")
            answer = input("=> ")
            if answer == "n":
                slowType("\n"
                    "So you chicken out? I did not expect that from you.\n")
                print(ascii_img.chicken)
                sys.exit()
            else:
                slowType("\n"
                    "Seems I meet a brave one, let's start...\n")
                clear()
                pick_story()


def pick_story():
    """ Allows the user to pick the main direction of the story, choosing between 3 options """
    global name
    print(f"\033[1;31;48m {ascii_img.house}")
    slowType(f"{lines_and_stories.intro}\n" 
    f"{name} {lines_and_stories.intro1}\n"
    f"{lines_and_stories.intro2}\n")
    clear()
    slowType(f"\033[1;31;48mTell me what do you think {name} will do now that is at home?\n")
    slowType("\n"
        " 1. Draw.\n 2. Do homework.\n 3. Take a nap.\n")
    stor_pick = input("\n""=> ")
    picked = ""
    if int(stor_pick) == 1:
        picked = lines_and_stories.story_picked[0]
        print(f"\033[1;31;48m{ascii_img.doing_art}")
        slowType(f"You were right, {name} headed to {picked}, so went to the studio.\n")
        story_draw()
    elif int(stor_pick) == 2:
        picked = lines_and_stories.story_picked[1]
        slowType(f"Yes, {name} headed to {picked}, so went to desk.\n")
        story_kitchen()
    elif int(stor_pick) == 3:
        picked = lines_and_stories.story_picked[2]
        slowType(f"Picked right there, {name} headed to {picked}, so went to the second floor.\n")
        story_closet()
    else:
        slowType("You had not pick a valid option, try again...\n")
        pick_story()


def story_draw():
    """
    Runs the option for the drawing story 
    """
    global name
    draw_pick = ""
    street_pick = ""
    clear()
    slowType(f"\033[1;31;48mEvery since was young {name} always had a power that\n"
        "had kept secret... whatever drew came true!\n"
        "Every day have played with Elizabeth, the best friend anyone\n"
        f"could have, they would play on magical creations that came\n"
        f"straight from {name}'s imagination, in castles, etc\n")
    print(ascii_img.princess)
    slowType(f"But as them got older, they grew apart.\n"
        f"{name} threw herself deeper into painting \n"
        "while Elizabeth played sports and started hanging out\n"
        "with other friend Jessica more often\n")
    print(ascii_img.basketball)
    clear()
    slowType("However, the two still maintained a tradition of meeting\n"
        "in front of school and walking home together until one day...\n"
        f"{name} was waiting for long time outside for Elizabeth,\n" 
        "but she still did not come.\n"
        "\n")
    clear()
    slowType(f"What should {name} do?\n")
    slowType("\n1. Go home.\n2. Go looking for Elizabeth.\n3. Go back into the school again and ask for more homework.\n")
    draw_pick = input("\n""=> ")
    if int(draw_pick) == 1:
        slowType("\n"f"{name} then went home, was enrange thinking that Elizabeth\n"
        "let her down. And passed the afternoon in bed upset.\n")
        at_school_next_day()
    elif int(draw_pick) == 2:
        slowType("\n"f"So {name} went looking for Elizabeth and walked and walked,\n"
        "until got in a strange street\n"
        "that never had been in before, suddenly ... she was lost!\n")
        slowType(f"What now... {name} though\n"
        "\n1. Yell for help?\n2. Keep walking.\n")
        street_pick = input("\n""=> ")
        if int(street_pick) == 1:
            slowType(f"So {name} did, and a lady respond and help so could make it back home\n")
            at_school_next_day()
        elif int(street_pick) == 2:
            slowType("\n"f"So that was the last time someone knew of {name},\n" 
            "only thing that was left were the draws...\n\n")
            print(ascii_img.end_banner)
            time.sleep(1)
            exit()
        else:
            slowType("That's not a valid option. Try again...\n")
    elif int(draw_pick) == 3:
        slowType("\n"f"{name} went then into the school and dedicate her time to homework.\n"
            "Never again draw or talk to anybody else.")
        clear()
        exit_app()
    else:
        slowType("\n""You had not pick a valid option, try again...\n")
        pick_story()


def at_school_next_day():
    clear()
    print("at school next day")
    slowType("And then it happened again the next day.\n After days and days of Elizabeth no showing up,\n Sarah confronted her at school"
    f"\033[1;36;40mWhy won’t you walk home with me?""she asked")
    slowType(f"\033[1;32;40mI walk home with Jessica now.""said Elizabeth\n"f"\033[1;32;40m It’s no big deal Sometimes things change.\n"
    f"{name} cursed at Elizabeth and screamed hateful\n""things heartbroken she ran home\n")


def story_kitchen():
    print("kitchen")


def story_closet():
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
    slowTypeF(ascii_img.end_banner)
    time.sleep(1)
    sys.exit()


welcome()
get_name()


#users_record = SHEET.worksheet("Sheet1")
#users_record.append_row(name)