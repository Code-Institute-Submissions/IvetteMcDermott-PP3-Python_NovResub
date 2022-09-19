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
    print(f"\033[1;31;40m {ascii_img.welcome}")
    slowType(f"\033[1;31;40m {lines_and_stories.WELC_LINE} \n")
    slowType("Only rule here is that you need to answer my questions \n"
    "where you see =>, so I can continue.\n")


def introduction():
    global name
    """ Collect the user"s name and validate it to no be empty """
    slowType("\n"
        "Now tell me your name ...\n")
    name = input("=> ")
    if name != "":
        time.sleep(3)
        slowType("\n"
            f"{name}, that name, it reminds me of a story...\n")
        age()
    else:
        slowType("You are not following the rules...\n")
        introduction()


def age():
    global name
    slowType("\n"f"but first, tell me your age {name}...\n")
    
    while True:
        age_input = input("=> ").strip()
        if not age_input.isdigit():
            slowTypeF("You are not following the rules."
            " You must enter a number.\n")
            continue
        age = int(age_input)
        if age > 99:
            slowTypeF("You not following the rules."
            "You must enter a number less than 100.\n")
            continue
        if age < 10:
            slowTypeF("Oh you are too young yet, sorry"
            " I may offer you in a next time a lullaby...\n")
            slowType(ascii_img.baby)
            slowType("Bye for now...")
            sys.exit()
        else:
            slowTypeF("ok, you are old enough but are you brave enough?\n")
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
                pick_story()


def pick_story():
    global name
    print(ascii_img.house)
    slowType(f"{lines_and_stories.intro} {name} {lines_and_stories.intro1}
    {lines_and_stories.intro2}")
    slowType("\n"f"Tell me what do you think {name} will do?\n")
    slowType("\n"
        " 1.Draw.\n 2.Do homework.\n 3.Take a nap.\n")
    slowType("\n"
        "Pick one (1 or 2 or 3)\n")
    stor_pick = input("=> ")
    picked = ""
    if int(stor_pick) == 1:
        picked = lines_and_stories.story_picked[0]
        slowType("\n"f"You were right, {name} headed to {picked}, so went to the art room.")
        story_draw()
    elif int(stor_pick) == 2:
        picked = lines_and_stories.story_picked[1]
        slowType("\n"f"Yes, {name} headed to {picked}, so went to desk.")
        story_kitchen()
    elif int(stor_pick) == 3:
        picked = lines_and_stories.story_picked[2]
        slowType("\n"f"Picked right there, {name} headed to {picked}, so went to the second floor.")
        story_closet()
    else:
        slowType("\n""You had not pick a valid option, try again...\n")
        pick_story()


def story_draw():
    global name
    draw_pick = ""
    street_pick = ""
    slowType("\n""Every since was young\n"
        f"{name} always had power that had kept secret... whatever drew came true!"
        "Every day have played with Elizabeth, the best friend anyone could have,\n"
        f"they would play on magical creations that came straight from {name}'s imagination\n"
        "But as them got older, they grew apart."
        f"{name} threw herself deeper into painting while Elizabeth played sports\n"
        "and started hanging out with other friend Jessica more often\n")
    slowType("However, the two still maintained a tradition of meeting in front of school"
        " and walking home together until one day...\n"
        f"{name} was waiting for long time outside for Elizabeth, but she still did not come.\n"
        f"What should {name} do?\n")
    slowTypeDif("1. Go home.\n 2. Go looking for Elizabeth.\n 3. Go back into the school again and ask for more homework.")
    draw_pick = input("=> ")
    if int(draw_pick) == 1:
        slowType("\n"f"{name} then went home, was enrange thinking that Elizabeth let her down."
        "And passed the afternoon in bed upset.")
        at_school_day_one()
    elif int(draw_pick) == 2:
        slowTypeDif("\n"f"So {name} went looking for Elizabeth and walked and walked until got in a strange street\n"
        "that never had been in before, suddenly ... she was lost!\n")
        slowType(f"What now... {name} though")
        street_pick = input("1. Yell for help?\n""2. Keep walking.\n")
        if int(street_pick) == 1:
            slowType(f"So {name} did, and a lady respond and help so could make it back home")
            at_school_next_day()
        elif int(street_pick) == 2:
            slowType(f"So that was the last time someone knew of {name}, only thing that was left were the draws...")
        else:
            slowType("That's not a valid option. Try again...")
    elif int(draw_pick) == 3:
        slowType("\n"f"{name} went then into the school and dedicate her time to homework.\n"
            "Never again draw or talk to anybody else.")
    else:
        slowType("\n""You had not pick a valid option, try again...\n")
        pick_story()


def at_school_next_day():
    print("at school next day")


def story_kitchen():
    print("kitchen")


def story_closet():
    print("closet")

#def no_valid_option():

welcome()
introduction()

#users_record = SHEET.worksheet("Sheet1")
#users_record.append_row(name)