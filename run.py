import gspread
from google.oauth2.service_account import Credentials

import ascii_img 
import lines_and_stories

import sys
import time
import os


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("pp3-python")


def slowType(data):
    """ Slow down the print time for one line, taken from tutorial, credit in README """

    for character in data:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(.1)
    return ""


def slowTypeF(data):
    """ Slow down the print time but continue, for long texts, taken from tutorial, credit in README """

    for character in data:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(.03)
    return ""

def slowTypeDif(data):
    """ Slow down the print time with 2 sets of time, taken from tutorial, credit in README """

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
    slowTypeF(f"\033[1;31;40m {ascii_img.welcome}")
    slowType(f"\033[1;31;40m {lines_and_stories.WELC_LINE} \n")
    slowType('Only rule here is that you need to answer my questions where you see =>, so I can continue.\n')


name = ''

def introduction():
    """ Collect the user's name and validate it to no be empty """
    slowType('\n'
        'Now tell me your name ...\n')
    name = input('=>')
    if name != '':
        time.sleep(3)
        slowType('\n'
            f'{name}, that name, it reminds me of a story...\n')
        age()
    else:
        slowType('You are not following the rules...\n')
        introduction()
    return name

def age():
    slowType('\n'f'but first, tell me your age {name}...\n')
    age = input('=>')
    if int(age) >= 10:
        slowType('\n'
            f'{age}?...you are old enough to hear it but are you brave enough?\n')
        slowType('\n'
            "Do you want to continue? 'y' for yes or 'n' for no \n")
        answer = input('=>')
        if answer == 'n':
            slowType('\n'
                'So you chicken out? I did not expect that from you.\n')
            print(ascii_img.chicken)
        else:
            slowType('\n'
                "Seems I meet a brave one, let's start...\n")
            pick_story()
    elif age == '':
        slowType('You are not following the rules...\n''Try again...')
        age()
    else:
        slowType('\n'
        'Oh you are too young yet, sorry I may offer you in a next time a lullaby...\n')
        slowType(ascii_img.baby)
        slowType('Bye for now...')


def pick_story():
    intro = lines_and_stories.introduction[0]
    intro1 = lines_and_stories.introduction[1]
    intro2 = lines_and_stories.introduction[2]
    print(ascii_img.house)
    slowType(f"{intro} {name} {intro1} {intro2}")
    slowType('\n''Now tell me what would you like do?\n')
    slowType('\n'
        ' 1.Draw in your room.\n 2.Do your homework.\n 3.Take a nap.\n')
    slowType('\n'
        'Now pick one (1 or 2 or 3)\n')
    stor_pick = input('=>')
    picked = ''
    if int(stor_pick) == 1:
        picked = lines_and_stories.story_picked[0]
        slowType('\n'f'You had picked "{picked}" {lines_and_stories.LETS_BEGIN}')
    elif int(stor_pick) == 2:
        picked = lines_and_stories.story_picked[1]
        slowType('\n'f'You had picked "{picked}" {lines_and_stories.LETS_BEGIN}')
    elif int(stor_pick) == 3:
        picked = lines_and_stories.story_picked[2]
        slowType('\n'f'You had picked "{picked}" {lines_and_stories.LETS_BEGIN}')
    else:
        slowType('\n''You had not pick a valid option, try again...\n')
        pick_story()
    story_part_one()


def story_part_one():
    print('ta-da')


welcome()
introduction()

# users_record = SHEET.worksheet("Sheet1")
# users_record.append_row(name)