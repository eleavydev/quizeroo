# Quizeroo - A simple and fun trivia quiz game!!

Quizeroo!! is a simple and fun trivia quiz game which allows a user to test their knowledge in a few different quiz topics. 

It can be played quickly, as there are only 10 questions per topic, many times throughout the day for fun and to keep their brain active! 

Users of this game will be able to view the rules of the game, play the game by choosing one of three topics (1. Father Ted 2. Music and 3. Geography), answering 10 questions per topic and see how they're doing as they progress through the game. 

As they answer each question, they are told 'Correct, Well Done!' or 'Incorrect, Hard Luck', so they are aware of their progress. 
At the end, their Actual Answers are displayed along with their Guesses and their Final Game Score is also given. 
Users are also given the choice to play again if they wish. 


![Screenshots of Quizeroo game](https://res.cloudinary.com/dlsbkq7mw/image/upload/v1660355525/Quizeroo/Welcome_Quizeroo_p2z0sp.png "Quizeroo - A simple and fun trivia game quiz") 

#### Live game can be found at: https://quizeroo.herokuapp.com/


## Features 
### Existing Features

The first iteration of Quizeroo is a simple command line interface/terminal game which allows the user to play the game...

* Read the rules.
* Choose a topic.
* Answer 10 questions on the topic.
* View their end score. 
* Choose to play again if they wish.

The user is kept informed of progress as they answer each question and at the end of the round are given a score in percent (i.e., Your score is: 50%). 

### Future Features

If I were to extend the game in future, I would add in below features. 

  - Extend the set of Quiz topics from 3 to 10, for variety of choice for the user. 
      - I would add in new topics: History, Sport, Literature, Films, Maths, Science, Fashion. 
  - Extend the set of questions from 10 per topic to 50 per topics.    
  - Prompt user to input more details: 
      - Enter name.
      - Choose number of questions to answer.       
      - Choose difficulty of game i.e., Low, Medium or High. 
  - Based on this user input, I would: 
       - Personalise messages using user's name. 
       - Dynamically set the number of questions asked per round according to user input. 
       - Output questions depending on their difficulty rating according to user input. 
       - Randomise order of questions so they are asked in different order every time. 
  
## Wireframe

I prepared a rough wireframe of how the game should look and its different areas. 
![Mockup](https://res.cloudinary.com/dlsbkq7mw/image/upload/v1657189220/Rock%20paper%20scissors/Wireframe_Rock_Paper_Scissors_lrrwq7.jpg) 

## The Welcome screen
The Welcome screen presents 3 different options to the user: 
1. Play Game.
2. Read Rules.
3. Quit. 

![Game](https://res.cloudinary.com/dlsbkq7mw/image/upload/v1660355525/Quizeroo/Welcome_Quizeroo_p2z0sp.png) 

## Quiz Rules

![Quiz Rules](https://res.cloudinary.com/dlsbkq7mw/image/upload/v1660354949/Quizeroo/Quiz_Rules_zjs2bm.png) 

  - The quiz rules introduce the user to the game. 
  - The quiz rules section aims to set the scene for the user and advise them what to expect throughout the game.  
  
## Choose Quiz Topic

![Choose Quiz Topic](https://res.cloudinary.com/dlsbkq7mw/image/upload/v1660354949/Quizeroo/Choose_Quiz_Topic_kol79r.png) 

 - The quiz topic section allows the user to choose the quiz topic they would like to answer questions on. 

## Question Time

![Question Time](https://res.cloudinary.com/dlsbkq7mw/image/upload/v1660354949/Quizeroo/Question_TIme_btn9mb.png) 

 - User is presented with the questions alongside 4 possible options (A, B, C or D). 
 - Input is validated so that only A, B, C or D as answers are accepted. 

## Results

![Results](https://res.cloudinary.com/dlsbkq7mw/image/upload/v1660354949/Quizeroo/Results_jlxiwg.png) 

 - User is presented with the actual answers alongside their guesses. 
 - User is also shown their score as a percentage, so they know how well they got on. 
 - User is then asked if they would like to play again.   
 - User can simply enter Y (Yes) or N (No) to play again. 

## Design choices

Certain design decisions were made to keep the game simple and fun. 

- Layout and wording are kept simple, easy to read and informal throughout the game. 

- Terminal is cleared periodically by calling clear_terminal() function so only the relevant game content is displayed. This keeps the screen easy to read and uncluttered. 

- Exclamation marks are used for some of the messaging to keep the game light and fun to keep the user engaged and entertained. 

- Questions are presented with multiple choice answers, so that the user can play the game with ease even if they don't know the answer (they can simply guess!). 

- Questions are kept fun and number of questions limited to 10, so that each game is very quick to run through. 

- User is kept informed of progress as they go through the game - i.e. they are told 'Correct, Well Done!' or 'Incorrect, Hard Luck' as they answer each and every question. This aims to keep the user engaged and informed throughout the game.  


## User Stories

- As a user I expect the game to be easy and enjoyable to play. 

- As a user I expect to see rules and clear instruction telling me what I need to do. 

- As a user I want only relevant content to be displayed at any one time. 

- As a user I want to be informed of the outcome as I answer each question. 

- As a user I want to be informed of my score at the very end of the game. 

- As a user I want to be informed of the right answers at the very end of the game. 

- As a user I want to be clear when the game is over. 

- As a user I want to know how to play the game again if I so wish. 


## Testing 

Manual Testing 

- I tested that this game works in different browsers: Edge, Chrome and Firefox. 

- I tested that the game loads correctly, presenting the user with the 3 options as required. (1: Play Game, 2: Read Rules and 3. Quit)

- I tested that the initial game logic works:

    - User Chooses 1: Play Game; Play Game sequence kicks off as expected. 

    - User Chooses 2: Read Rules; Rules are displayed with an option to press Enter to continue. This brings user back to Initial Menu. 

    - User Chooses 3: Quit; they are presented with a goodbye message.

- I tested that user inputs are validated, so that the user is forced to input the correct options 
    (Options 1, 2 or 3 for Initial Game and Topic Choice).
    (Options A, B, C or D when answering questions).
    (Options Y (Yes) or N (No) when indicating if they'd like to play again).

- I confirmed that the messaging is clear, consistent, easy to read and makes sense. 

- I confirmed that the terminal clears periodically so that only relevant messaging displays. 

- I confirmed that the user is told after every question whether they were Correct or Incorrect. 

- I confirmed that the user is shown their score at the end of the game. 

- I confirmed that the user can choose to play again if they wish to. 

- I asked friends and family to play to confirm that the game logic works and questions and answers are accurate. 


Solved Bugs 
- Initially the .json Question files were not being opened and read in correctly. 
    - Filenames were not being initialised correctly in the code and therefore could not be opened correctly.  
- System logic wasn't functioning correctly initially. 
    - I debugged, using prints to see where the code was going wrong. Fixed as required. 
- Player's guess was displaying as incorrect, even though it was correct. 
   - System was comparing lowercase and uppercase letters and finding them to be different, so I needed to use upper() function before comparing inputs. 
- System was crashing if user inputs invalid option like '5/y/7/*/t' before Yes (Y) or No (N). 
    - Located the error and fixed as required. 
- Cosmetic issue: Some of the Menu items and game messaging appeared to be out of alignment.
    - Fixed as required by removing/inserting spaces to re-balance appearance of text. 
- Cosmetic issue: Some spelling mistakes were noticed in game messaging. 
    - Fixed as required.
-   When I ran through PEP8, I found that I was missing some spaces after function calls
    - Fixed as required by adding in spaces where necessary.  


### Validator Testing 

- PEP8 Compliance
  - No errors were returned upon passing through official [PEP8 Online](http://pep8online.com/checkresult) Validator  
  ![Results](https://res.cloudinary.com/dlsbkq7mw/image/upload/v1660356984/Quizeroo/PEP8_Compliance_xrkzct.png) 


### Unfixed Bugs

No Unfixed bugs. 

## Deployment

- My Source Code on GitHub is available at: [eleavyGitHub](https://github.com/eleavydev/quizeroo)  

- My live deployed project is available at [Quizeroo](https://quizeroo.herokuapp.com/)  

### Cloning and Forking  

1. Cloning

- Go to my GutHub repository at: [eleavyGitHub](https://github.com/eleavydev/quizeroo). 
- Click on the Green "Code" drop down. 
- Choose to either Download the code as a Zip file or Clone manually using Gitlink provided. 

2. Forking

- Go to my GitHub repository at: [eleavyGitHub](https://github.com/eleavydev/quizeroo). 
- Click the Fork button at the top right of the page and wait for a few seconds. 
- You will see that this newly forked repository gets created under your GitHub account.  


### Deployment 

- Navigate to Heroku website [Heroku] https://dashboard.heroku.com/ and either sign in or click sign up to create a new account.
- In your account dashboard click the Create new APP button.
- Add a name for APP in the APP-Name field.
- Select your region from the drop-down menu and click on Create APP button.
- On the next page click on the Settings tab to adjust the settings.
- Click on the "config vars" button and hide any sensitive files from being deployed.
- In the field for key add the sensitive file name and in the value field copy the entire   file from your workspace into this field and click add.
in the supply key field below this add PORT and 8000 into the value field. Then click on the "add" button.
- Click on the ADD Buildpack button.
- Select python buildpack and click save changes. Then click Add Buldpack button again but this time add node.js and save changes. Please ensure that you are adding them in this order as it may cause issues otherwise.
- Navigate to the deploy section by using the deploy tab a the top of the screen, select Github and connect to your Github profile.
- Search for your Github repo name by adding the name to the repo-name tab and click the search button.
- When the search is complete, click on the connect button to the right of your repo name.
- Now you can deploy the app automatically or manually. Automatically deploy will update the app automatically every time you push any changes to Github.
- Once the build is successful, you can open the app by clicking Open App button in the top right corner.
  

## Credits 

### Content 

- Thanks to Code Institute for the deployment template. 
- The quiz questions and game instructions were created by myself. 
- The Love Sandwiches and Code Institute projects were both used as great guides to help with this project. 
- Websites such as [Stackoverflow](https://stackoverflow.com/), [CommunitySpiceworks](https://community.spiceworks.com/) were consulted for help with this project. 
- As always, my mentor Chris was very patient and encouraging during this process. His tips re: finding out about and using time.sleep(1) and clear terminal function were very useful. 
- Also, our Cohort facilitators Kenan and Kasia along with classmates and peers on Slack and tutor support were very helpful to draw on for support. 

### Media

- Screenshots for this page were hosted on [Cloudinary](https://cloudinary.com/)
