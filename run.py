import gspread
from google.oauth2.service_account import Credentials

import time
import ascii_img 

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

print(ascii_img.welcome)

name = str(input("Tell me your name ..."))


try: 
    time.sleep(5)
    print('That name reminds me of a story... mmm...')
    time.sleep(5)
except:
    name == "" or name == " "
    print('You need to tell me your name...')
    time.sleep(5)    


age = input('but first tell me your age...')
time.sleep(10)
print('ok... you are old enough to hear it but are you brave enough?.')
brave = input('Y for yes and N for no...')

if brave == 'Y':
    time.sleep(3)
    print('Which would you prefer...?')
    pick_story()
elif brave=='N':
    time.sleep(2)
    print("So you chicken out? I didn't expect that from you")
    print(ascii_img.chicken)
    print('Maybe one day I should offer a lullaby?')
    print(ascii_img.baby)
