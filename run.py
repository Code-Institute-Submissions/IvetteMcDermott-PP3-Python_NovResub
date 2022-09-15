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

trial = SHEET.worksheet("Sheet1")
trial_values = trial.get_all_values()


def slowType(data):
    """ Slow down the print time, taken from tutorial, credit in README """

    for character in data:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(.1)
    return ""


def slowTypeF(data):
    """ Slow down the print time, taken from tutorial, credit in README """

    for character in data:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(.03)
    return ""

def slowTypeDif(data):
    """ Slow down the print time, taken from tutorial, credit in README """

    for character in data:
        sys.stdout.write(character)
        sys.stdout.flush()
        if character != "\n":
            time.sleep(.1)
        else:
            time.sleep(1)
    return ""


def welcome():
    slowTypeF(f"\033[1;31;40m {ascii_img.welcome}")
    slowType(f"\033[1;31;40m {lines_and_stories.WELC_LINE} \n")


def introduction():
    slowType('Now tell me your name ...')
    name = input('=>')
    if name != '':
        time.sleep(3)
        slowType(f'{name}, that name, it reminds me of a story...\n')
        age()
    else:
        slowType('You are not following the rules...')
        introduction()


def pick_story():
    slowType('Tell me which one would you like me to tell you? pick a number\n')
    slowType('1. The Disembodied Voice. \n  2.Do not turn out the lights.\n  3.The Scratches in the Closet\n')
    stor_pick = input('=>')
    picked = ''
    if int(stor_pick) == 1:
        picked = lines_and_stories.story_picked[0]
        slowType(f'You had picked "{picked}"')
    elif int(stor_pick) == 2:
        picked = lines_and_stories.story_picked[1]
        slowType(f'You had picked "{picked}"')
    elif int(stor_pick) == 3:
        picked = lines_and_stories.story_picked[2]
        slowType(f'You had picked "{picked}"')
    else:
        slowType('You had not pick a valid option, try again...')
        pick_story()


def story_part_one():
    print('ta-da')


def age():
    slowType('but first, tell me your age...\n')
    age = input('=>')
    if int(age) >= 10:
        slowType(f'{age}?...you are old enough to hear it but are you brave enough?\n')
        slowType("Do you want to continue? 'y' for yes or 'n' for no \n")
        answer = input('=>')
        if answer == 'n':
            slowType('So you chicken out? I did not expect that from you.\n')
            print(ascii_img.chicken)
        else:
            slowType("Seems I meet a brave one, let's start...\n")
            pick_story()
    else:
        slowType('Oh you are too young yet, sorry I may offer you in a next time a lullaby...\n')
        slowType(ascii_img.baby)
        slowType('Bye for now...')


welcome()
introduction()


"""slowprint("It's time for me to tell you some spooky stories... but first,...\n")
name = slowprint('Tell me your name ...\n')"""


"""
def get_name(name):
    name = get_name('Tell me your name ...\n')
    validation_input(name)    
    return name

def get_age(prompt):
    return int(input(prompt))

def validation_input(name):
     idea took from love-sandwiches
        to manage data no empty
    
    while name != '':
        print(f'{name}... That name reminds me of a story... mmm...')
        get_age('but first, you need to tell me your age...')
        return name
    else:
        print('You need to tell me your name...\n')
        get_name(name)


validation_input(name)

# time.sleep(4)

    

# time.sleep(4)
# print(f'{age}?...you are old enough to hear it but are you brave enough?\n')
# brave = input('"y" for yes and "n" for no...\n')

# if brave == 'y':
#     time.sleep(3)
#     print('Which would you prefer...?\n')
#     # pick_story()
# elif brave == 'n':
#     time.sleep(2)
#     print("So you chicken out? I didn't expect that from you.\n")
#     print(ascii_img.chicken)
#     print('Maybe one day I should offer a lullaby?\n')
#     print(ascii_img.baby)
"""
