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

        if character != "\n":
            time.sleep(.1)
        else:
            time.sleep(1)

os.system("cls")


