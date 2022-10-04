![](https://res.cloudinary.com/dwjq6izv5/image/upload/v1664817563/PP1/PP3%20/welcome_and_name_rl1wcq.png)

# **SPOOKY STORIES**

[🖥️ LIVE SITE](https://pp3-python.herokuapp.com/)
<br>

This site was inspired by interactive e-books, the spooky theme is down to the Halloween season. Developed as a type of campfire spooky story, the target users are children over 9 years old. The site in certain stages of the story present options to the user to make decisions and lead the story to one of the alternative endings.

The goal of this website is promoting reading and making decisions through an interactive adventure in an engaging way.
<br>

## **UX**
<br>

### **Ideal User**

English speaking children 10+ years old that enjoy spooky stories.
<br>

### **First Time User Goals**

As a first time user, I want to find it easy to understand the purpose of the site.
As a first time user, I want to find it easy to understand the way to interact with the site.
As a first time user, I want to understand that there are multiples outcomings that could open if I return.
<br>

### **Returning User Goals**

As a returning user, I want to find twists in the story.
As a returning user, I want to see the different endings of the story.
<br>

### **Flowchart**
<br>

![](https://share.balsamiq.com/c/rX1TCfGCoBMT2giNVCjCkv.png)
<br>

## **Design**
<br>

Being the theme of the app "Spooky Stories" and down to the Halloween season being so close. The app colors had been picked to go with it.  Purple and black, mainly these colors are use often in children's spooky stories and are appropiate for the season.
A background image had been set in html for the body, it corresponds to a haunted house in the theme colors picked. Some CSS had been added and modified for the size of the terminal, padding, the button, and other minor adjusts for a better visual experience. 

The terminal keeps the black background and the text had been set to purple. Also some other colors had been used for texts that belong to a character.  The decisions in the game had been kept in purple as was most of the text, considering that all is being relayed by the narrator.

The text is kept to a few lines by screen, and the clean screen function has a delay of 3 seconds to give time to the user to read and observe the ascii arts.

## **Features**
<br>

The terminal displayed is the default from the CI template with some minor adjustements for better visual according to the idea of the project.
<br>
<br>

Welcome Screenshot
<br>

![](https://res.cloudinary.com/dwjq6izv5/image/upload/v1664817657/PP1/PP3%20/Welcome_SS_wxjmri.png)
<br>

Request Name Input and Age Input and shows the validation on them
<br>

![](https://res.cloudinary.com/dwjq6izv5/image/upload/v1664817566/PP1/PP3%20/age_validation_for_over_99_jqaszr.png)
<br>

Validation for under 9s, as the story is for 10+
<br>

![](https://res.cloudinary.com/dwjq6izv5/image/upload/v1664817563/PP1/PP3%20/age_validation_under_10_nyr2xc.png)
<br>

Screenshot of the decision of no start the story
<br>

![](https://res.cloudinary.com/dwjq6izv5/image/upload/v1664817566/PP1/PP3%20/confirmation_to_start_pick_no_to_u571zg.png)
<br>

Screenshot of the format for multiple options presented to the user
<br>

![](https://res.cloudinary.com/dwjq6izv5/image/upload/v1664817561/PP1/PP3%20/first_decision_to_make-direction_mihxtl.png)
<br>

Screenshot of the format for yes or no options presented to the user
<br>

![](https://res.cloudinary.com/dwjq6izv5/image/upload/v1664895882/PP1/PP3%20/yes_or_no_pnz55a.png)
<br>

Screeshot of The End screen
<br>

![](https://res.cloudinary.com/dwjq6izv5/image/upload/v1664817558/PP1/PP3%20/end_screen_uh7mnt.png)
<br>

### **Features to implement in future**

More options and twists could be added to it, to increase and extend the adventure. To encourage the users to return.
<br>

## **Technologies Used**
<br>

- [Python](https://www.python.org/)
- [GitHub](https://github.com/)
- [GitPod](https://www.gitpod.io/)
- [Heroku](https://www.heroku.com/about)
- [LucidCharts](https://www.lucidchart.com/pages/)
- [Cloudinary](https://cloudinary.com/)
<br>

## **Testing**
<br>
The site had been tested in Chrome, Firefox and Edge without noticable trouble.  
Safari won't run the app but it shows it, seen that I reached Tutor Assistance and the answer was that the terminal won't run on OS or Mobile so it should be expected and to mention it.
<br>

![](https://res.cloudinary.com/dwjq6izv5/image/upload/v1664902140/PP1/PP3%20/safari_ss_dj6j2z.png)
<br>

### **Validation**

At the moment of concluding the project the site pep8 still down, for that reason I got in touch with Tutor Assistance and Student Support both guided me into using the pycodestyle built in my workspace in gitpod, path that I followed and resulting as the screenshot below shows.
<br>

![](https://res.cloudinary.com/dwjq6izv5/image/upload/v1664881623/PP1/PP3%20/linter_in_terminal_py_kaqyk7.png)
<br>

Linter shows no error for run.py file. Howsoever it shows three warnings related to ms-toolsai.jupyter extension and .gitpod.yml but these are not part of the code, or anything that interferes with the app so they had been left alone as talked with Tutor Assistance.

It also shows no errors for the file lines_and_stories.py. Instead for the ascii_img.py shows up to 30 errors but this is down to the file containing ascii arts which the linter does not recognise, at the begining there were over 72 errors but they were reduced with minor modifications in the arts, but those had been left as the visual would be affected.
<br>

![](https://res.cloudinary.com/dwjq6izv5/image/upload/v1664882598/PP1/PP3%20/linter_in_ascii_arts_py_g4wr4t.png)
<br>

The validation for layout.html shows no error, this had been run as there were small modifications made on it for better visual.
<br>

![](https://res.cloudinary.com/dwjq6izv5/image/upload/v1664882792/PP1/PP3%20/validator_html_w6qvpv.png)
<br>

### **Manual Testing**
<br>

| Feature | Test Action | Validation for Wrong Input  | Test Outcome |
|:---|        :---| :---|:---|
| Name Input | Type in user's name | Check if empty | Pass |
| Age Input | Type in user's age | Check if age is between 10 and 99, or empty | Pass |
| Confirm to start | Choose y or n | Check that there is no different or empty input than the expected | Pass |
| Pick between three options "Decision main" | Choose 1, 2 or 3 | Check that there is no different or empty input than the expected| Pass |
||

If picked 1 in "Decision Main"
| Feature | Test Action | Validation for Wrong Input  | Test Outcome |
|:---|        :---| :---|:---|
| Pick between three options "Decision After School" 1 | Choose 1, 2 or 3 | Check that there is no different or empty input than the expected | Pass |
| Pick between three options "Decision After School" 2 | Choose 1 or 2 | Check that there is no different or empty input than the expected | Pass |
| Pick between three options "Decision Lost" | Choose 1 or 2 | Check that there is no different or empty input than the expected | Pass |
||

If picked 2 in "Decision Main"
| Feature | Test Action | Validation for Wrong Input  | Test Outcome |
|:---|        :---| :---|:---|
| Pick between two options "Decision Is Mom Home" | Choose 1 or 2 | Check that there is no different or empty input than the expected | Pass |
| Pick between two options "Decision Go Downstairs" | Choose 1 or 2 | Check that there is no different or empty input than the expected | Pass |
||

If picked 3 in "Decision Main"
| Feature | Test Action | Validation for Wrong Input  | Test Outcome |
|:---|        :---| :---|:---|
| Display text and lead to one of the ends | -- | -- |Pass |
||||

<br>

## **Deployment**
<br>
The site had been deployed through Heroku. 

The site had been developed on GitPod, committed and pushed to GitHub. And Heroku once the site is deployed would update automatically.

Deployment proccess:

1. Log in [Github](https://github.com/).
    - Open the repo to deploy. The one for the site is [here](https://github.com/IvetteMcDermott/PP3-Python).
2. Log in [Heroku](https://www.heroku.com/).
    - Click in the "New" button in the top right.
    - Select "Create New App"
    - Give a name to the App and choose a region.
    - Click in "Create App" button.
    - Go to Settings in the nav bar, and select "Add Buildpacks".
    - Add Python and save, do the same for Node.js, in that order. Python must show first in the list.
    - Go to Deploy in the nav bar. In Deploment Method, select GitHub/Connect to GitHub.
    - In Connect to GitHub, write the repository name and click in search.
    - Once the route for the repo appears under the search, click in "Connect" button.
    - The deployment can be Manual or Automatic, select the one of your preference. Automatic has the advantage of updating your deployed site as you push the commit in GitHub.
    - Verify that "Branch to deploy" is master/main.
    - Click Deploy.

Steps to use and deploy this repository:

- Access to the repo in GitHub [here](https://github.com/IvetteMcDermott/PP3-Python).
- It can be "Fork" following the steps [here](https://docs.github.com/en/get-started/quickstart/fork-a-repo).
- It can be "Clone" following the steps [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository).
<br>

## **Credits**
<br>

### **Text**
The stories had been taken and modified from the video "8 Scary Ghost Stories (Don't watch alone...)" from the YouTube Channel [Peacock Kids](https://youtu.be/gh0BD4Ut9Tw) 
<br>

### **Arts**
The arts and banners had been taken and created with 

- [EmojiCombos](https://emojicombos.com/monster-ascii-art)
- [ManyTools](https://manytools.org/hacker-tools/ascii-banner/)
- [Ascii Art](https://www.asciiart.eu/)
- [Wallpaper Flare](https://www.wallpaperflare.com/4k-moon-haunted-house-bats-wallpaper-uhagw)
<br>

### **Code**
- [Learn learn Scratch Tutorials](https://www.youtube.com/watch?v=2h8e0tXHfk0) Code for slow typing.
- [Rick Atherton](https://github.com/RickofManc/vv-pizzas) Code for clean screen.
- Also thanks to my mentor Brian Macharia, who had guided me in the project and especially in the refactoring on the validation of my age function.
<br>

