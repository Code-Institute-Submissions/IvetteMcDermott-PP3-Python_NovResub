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
    slow_type("The only rule here is that you need to answer my questions \n"
              "where you see =>, so we can continue.\n")


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
    global name
    slow_type("but first, tell me your age...\n")
    while True:
        age_input = input("=> ").strip()
        if not age_input.isdigit():
            slow_type("You are not following the rules."
                      " You must enter a number.\n")
            continue
        if (int(age_input)) > 99:
            slow_type("You not following the rules."
                      "You must enter a number less than 100.\n")
            continue
        if (int(age_input)) < 10:
            slow_type("Oh you are too young yet, sorry"
                      " I may offer you a lullaby next time...\n")
            slow_type(ascii_img.BABY)
            slow_type("Bye for now...")
            sys.exit()
        else:
            slow_type("\n"
                      "ok, you are old enough but are you brave enough?\n")
            confirm_continue()


def confirm_continue():
    """
    Confirm if user wants to start the story or decide to leave
    """
    slow_type("\n"
              "Do you want to continue? 'y' for yes or 'n' for no \n")
    answer = input("=> ")
    if answer == "n":
        slow_type("\n"
                  "So you chickened out?\n"
                  "I did not expect that from you.\n")
        print(ascii_img.CHICKEN)
        exit_app()
    elif answer == 'y':
        slow_type("\n"
                  "Seems I met a brave one, let's start...\n")
        clear()
        pick_story()
    else:
        slow_type("That's not a valid option. Try again...\n")
        confirm_continue()


def pick_story():
    """ Allows the user to pick the main direction of the story,
    choosing between 3 options
    """
    print(f"\033[1;31;48m {ascii_img.HOUSE}\n")
    slow_type(f"{lines_and_stories.introduction[0]}\n"
              f"{name} {lines_and_stories.introduction[1]}\n"
              f"{lines_and_stories.introduction[2]}\n")
    clear()
    slow_type(f"\033[1;31;48mTell me what do you think {name} will do"
              " now that they are at home?\n")
    slow_type("\n"
              " 1. Draw.\n 2. Do homework.\n 3. Take a nap.\n""\n")
    stor_pick = input("=> ")
    picked = ""
    if int(stor_pick) == 1:
        picked = lines_and_stories.story_picked[0]
        print(f"\033[1;31;48m{ascii_img.DOING_ART}")
        slow_type(f"You were right, {name} headed to {picked},"
                  " so they went to the studio.\n")
        story_draw()
    elif int(stor_pick) == 2:
        picked = lines_and_stories.story_picked[1]
        slow_type(f"Yes, {name} headed to {picked}, so they went to "
                  "work at their desk.\n")
        story_kitchen()
    elif int(stor_pick) == 3:
        picked = lines_and_stories.story_picked[2]
        slow_type(f"Picked right there, {name} headed to {picked},"
                  " so went to the second floor.\n")
        story_closet()
    else:
        slow_type("That's not a valid option. Try again...\n")
        pick_story()


def story_draw():
    """
    Runs the option for the drawing story
    """
    draw_pick = ""
    street_pick = ""
    clear()
    slow_type(f"\033[1;31;48mEvery since was young {name} "
              "always had a power that\n"
              "had kept secret... whatever drew came true!\n"
              f"Every day {name} had played with Elizabeth, the best friend\n"
              "anyone could have, they would play on magical creations that\n"
              f"came straight from {name}'s imagination.")
    print(ascii_img.PRINCESS)
    slow_type("\n""\033[1;31;48mBut as they got older, they grew apart.\n"
              f"{name} threw themself deeper into painting.\n")
    time.sleep(1)
    clear()
    slow_type("\n \033[1;31;48mWhile Elizabeth played sports and started"
              " hanging out\n"
              "with another friend, Jessica, more often\n")
    print(ascii_img.BASKETBALL)
    slow_type("\n"
              "However, the two still maintained a tradition of meeting\n"
              "in front of school and walking home together until"
              " one day...\n")
    clear()
    slow_type(f"\033[1;31;48m{name} was waiting for long time outside for"
              " Elizabeth,\n""but she still did not come.\n"
              "\n")
    slow_type(f"\033[1;35;48mWhat should I do?"
              f" \033[1;31;48mThough {name}\n")
    slow_type("\n1. Go home.\n2. Go looking for Elizabeth.\n3. Go back into"
              " the school again and ask for more homework.\n""\n")
    draw_pick = input("=> ")
    if int(draw_pick) == 1:
        slow_type("\n"f"{name} then went home, and was enranged thinking that"
                  " Elizabeth\n"
                  "forgot about it. So passed the afternoon in bed upset.\n")
        at_school_next_day()
    elif int(draw_pick) == 2:
        slow_type("\n"f"So {name} went looking for Elizabeth, and walked\n"
                  " and walked... until they got into a strange street\n"
                  "that they had never been in before, suddenly ..."
                  f" {name} was lost!\n")
        slow_type(f"What now... {name} though\n"
                  "\n1. Yell for help?\n2. Keep walking.\n""\n")
        street_pick = input("=> ")
        if int(street_pick) == 1:
            slow_type(f"So {name} did, and a lady responded and helped"
                      " so they could make it back home\n")
            at_school_next_day()
        elif int(street_pick) == 2:
            slow_type("\nSo that was the last time someone heard of \n"
                      f"{name}, the only things that were left "
                      "were the drawings...\n")
            print(ascii_img.END_BANNER)
            exit_app()
        else:
            slow_type("That's not a valid option. Try again...\n")
    elif int(draw_pick) == 3:
        slow_type("\n"f"\033[1;31;48m{name} went into the school and"
                  " dedicate their time to homework.\n"
                  "Never again drew or spoke to anybody else.""\n")
        print(ascii_img.END_BANNER)
        exit_app()
    else:
        slow_type("That's not a valid option. Try again...\n")
        pick_story()


def at_school_next_day():
    """
    Display next part of the story draw
    """
    clear()
    slow_type(f"\033[1;31;48mAnd then it happened again the next day.\n"
              "After days and days of Elizabeth not showing up,\n"
              f"{name} confronted her at school\n""\n"
              f"\033[1;36;48mWhy won't you walk home with me?"
              f"\033[1;31;48m they asked\n""\n"
              f"\033[1;32;48mI walk home with Jessica now. "
              f"\033[1;31;48msaid Elizabeth\n"
              f"\033[1;32;48mIt's no big deal sometimes things change.\n""\n"
              f"\033[1;31;48m{name} yelled at Elizabeth and screamed hateful\n"
              "things and heartbroken, ran home\n")
    clear()
    slow_type("\033[1;31;48mAfter thinking about it a while, Elizabeth"
              " felt bad for abandoning her friend,"
              " so she decided to go to {name}'s house\n"
              "\n""What do you think will happen?\n""\n"
              "1. Make peace.\n 2. It was too late.\n""\n")
    next_day_selection = input("=> ").strip()
    if next_day_selection == "1":
        slow_type("They talked and fixed it, and returned to being friends,"
                  " understading their different interests.")
        print(ascii_img.END_BANNER)
        exit_app()
    elif next_day_selection == "2":
        slow_type(f"Elizabeth walked to {name}'s house ... but it was too"
                  " late...\n")
        clear()
        slow_type(f"\033[1;31;48mShe knocked on the door and {name} opened"
                  " and let her in,""\n"
                  "said was going to get lemonade, so told Elizabeth\n"
                  "\033[1;36;48m You can go to my room while I get it""\n"
                  "\033[1;31;48mBut Elizabeth for some reason headed to "
                  "the studio" "\n"
                  "and just as she was sitting at the desk, she saw"
                  " something that shocked her!\n""\n"
                  "she couldn't believe it! She had to run to see "
                  "Jessica now!!\n"
                  "So she did. When she got to Jessica's home"
                  " she even didn't \n"
                  "stop to say hello to her parents, she ran upstairs and \n"
                  "there she was...Jessica...Just like the drawing"
                  " in her hand...")
        clear()
        slow_type("\033[1;31;48mThere was Jessica in front her eyes, laying"
                  " in bed, tears on her cheeks ...she had no mouth!""\n""\n")
        print(f"{ascii_img.GIRL}""\n")
        clear()
        print(ascii_img.END_BANNER)
        exit_app()
    else:
        print("That's not a valid option. Try again...\n")
        at_school_next_day()


def story_homework():
    """
    Starts the kitchen story option
    """
    clear()
    slow_type("But the house was quiet after school now. Noone was there."
              f"So {name} settled in to began the homework"
              "waiting for her mom to get back home. Her dog sat beside her.\n"
              f"{name} had just finished her first math problem when "
              "she heard the door slam downstairs. Mom must be home early.\n"
              f"{name} called down to her, 'Mom?'\n")
    slow_type(f"Do you think was {name}'s mom? 'y' for yes or 'n' for no \n")
    answer_mom_arrived = input("=> ").strip()
    if answer_mom_arrived == "y":
        slow_type(f"Yes! Mom was home, and as soon as {name} end the homework,"
                  "they had dinner and saw a movie in family, together"
                  " with dad.")
        print(ascii_img.END_BANNER)
        exit_app()
    elif answer_mom_arrived == "n":
        slow_type("Right, noone respond...\n"
                  "Probably just the wind, thought.\n"
                  "And continues the homework. An hour past, almost finished "
                  "the first assignment when faintly heard the sounds \n"
                  "of pots and pans clanging downstairs.\n"
                  "But ...\n"
                  "She hadn't heard mom come in the door."
                  f"Disembodied voice: {name}"
                  "A voice called from downstairs")
        clear()
        slow_type(f"One second {name} distractely responded, finishing up "
                  "a final math problem\n"
                  f"Disembodied voice: {name}\n"
                  "The voice called again\n"
                  f"Will {name} go downstairs or notice something was"
                  " not right? 'y' for yes or 'n' for no")
        answer_go_downstairs = input("=> ").strip()
        if answer_go_downstairs == "n":
            slow_type(f"{name} realise that the voice was not mom!\n"
                      "So called: Moooom?\n"
                      "No answer... "
                      f"{name} ran lock the door and hide under the bed..."
                      "Hoping that soon enough someone arrive.")
            print(ascii_img.END_BANNER)
            exit_app()
        elif answer_go_downstairs == "y":
            slow_type(f"{name} closed the books and walk downstairs, "
                      "calling her dog to follow but he wouldn't budge.\n"
                      "She shrugged it off and walked downstairs and "
                      "into the kitchen.\n"
                      "No one was there but what she saw sent a chill "
                      "down her spine.\n"
                      "Every pot and pan in the house had been stacked "
                      "neatly in the middle of the room.\n"
                      "Cabinets lay open and empty."
                      "*She heard the sound of a creaking door*")
            clear()
            slow_type("The side door flew open beside her.\n"
                      f"In the doorway stood {name}'s mom, groceries in hand."
                      "But if she was only just getting home, "
                      "who laid out the pots and pans?  Mom looked around "
                      "at the scattered pots and pans, confused."
                      "'You helping me cook tonight, Chrissie?'"
                      f"'I didn't do this' replied {name}, as she and her"
                      " mom looked around the kitchen…"
                      "'Then who did?' asked her mom"
                      f"Disembodied voice: {name} dinner is ready")
        else:
            print("That's not a valid option. Try again...\n")
            story_homework()
    else:
        print("That's not a valid option. Try again...\n")
        story_homework()


def story_nap():
    """
    Open the flow to the closet story
    """
    slow_type(f"It was night when {name} woke to a strange noise "
              "sound coming from the closet...\n"
              "The rest of the house was quiet, but that noise...")
    print(ascii_img.END_BANNER)
    exit_app()


def clear():
    """
    Clears the screen for the next content to be display
    taken from RickofManc/vv-pizzas
    """
    time.sleep(1)
    print("\033c")


def exit_app():
    """
    Display the end banner, and exit the app after a second
    """
    slow_type("\n""\n"
              f"\033[1;31;48m{ascii_img.END_BANNER}")
    time.sleep(1)
    sys.exit()


welcome()
get_name()
