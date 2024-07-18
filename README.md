![logo](static/img/justask.png)


# ***JustAsk Blog - Pp4***
![am responsive]()
# **1. Key project information**

- **Description :** **Just ask** is a question-and-answer website where users can ask questions, answer questions, and interact with other users.
- **Key project goal :** To familiarize visitors of this page with **justask** blog
- **Audience :** Target audience are users that are using search engines to ask quetions and those who are looking for answers from various topics
- **Live version :** Live version of **Just Ask** page can be viewed at [JustAsk](https://just-ask-b3c36fe12bcc.herokuapp.com/).

![Mockup]()

---

## Table of Contents
+ [UX](#ux "UX")
  + [Site Purpose](#site-purpose "Site Purpose")
  + [Audience](#audience "Audience")
  + [Communication](#communication "Communication")
  + [Current User Goals](#current-user-goals "Current User Goals")
  + [New User Goals](#new-user-goals "New User Goals")
  + [Future Goals](#future-goals "Future Goals")
+ [Design](#design "Design")
   + [Flowchart](#flowchart "Flowchart")
+ [Features](#features "Features")
  + [Existing Features](#existing-features "Existing Features")
    + [Start game](#start-game "Start game")
    + [Game Rules](#game-rules "Game Rules")
    + [Enter Country Location](#enter-country-location "Enter Country Location")
    + [Enter Username](#enter-username "Enter Username")
    + [Possible Outcomes](#possible-outcomes "Possible Outcomes")
    + [Points Earned](#points-earned "Points Earned")
    + [Score](#Score "Score")
    + [Replay and Exit](#replay-and-exit "Play Again or Quit App")
  + [Features Left to Implement](#features-left-to-implement "Features Left to Implement")
+ [Testing](#testing "Testing")
  + [Validator Testing](#validator-testing "Validator Testing")
  + [Manual Testing](#manual-testing "Manual Testing")
  + [Bugs](#bugs "Bugs")
  + [Remaining Bugs](#remaining-bugs "Remaining bugs")
+ [Technologies Used](#technologies-used "Technologies Used")
  + [Main Language](#main-language "Main Language")
  + [Frameworks, Libraries & Programs](#frameworks-libraries-programs "Frameworks, Libraries & Programs")
+ [Deployment](#deployment "Deployment")
    + [Version Control](#version-control "Version Control")
    + [Page Deployment](#page-deployment "Page Deployment")
    + [Frok](#fork "Fork")
    + [Clone](#clone "Clone")
+ [Credits](#credits "Credits")
  + [Content](#content "Content")
  + [Acknowledgements](#acknowledgements "Acknowledgements")

## UX

### Site Purpose:
To provide a simple and fun platform where the user can play while learning about python through quiz and multi-choice answers.

### Audience:
Python learners, anyone who is interessed in learning python, it can be a programmer from a different language who wants to divert to python too. 

### Communication:
The game interface employs clear and colored print statements, ensuring an error-free and engaging gaming experience. These added colors enhances text readability and adds a visually appealing element to the game.

### Current User Goals:
The primary goal for current users is to be entertained and engaged in playing while learning something productive at the same time playing multiple rounds of the quiz Game will help the user master alot of python rules, it will help the user love python before stating to code. 

### New User Goals:
New users are encouraged to experiment with the computer-based version of the python quiz game and widen there python knowledge, the multi-choice answers helps them to guess the correct answer from the given options.

### Future Goals:
Make the game more challenging by introducing multiple difficulty levels for the user to choose to play and implementing a scoring leaderboard. 

[Back to top](<#table-of-contents>)

## Project Management

### Kanban Board & User Stories
I've been using the application [Kanban Board](https://trello.com/) and the project board in GitHub to keep my project together. It has been working really well and has helped me structure up my work a lot. Trello was used on a more general plan and GitHub was used to plan and organize my user stories.

<details><summary><b>Trello & Github Board</b></summary>

![Kanban Board](readme/assets/images/trello.png)

![User Stories](readme/assets/images/user_stories.png)
</details><br/>

[Back to top](<#table-of-content>)

### Database Schema
I have used a modelling tool called [Graph Models](https://django-extensions.readthedocs.io/en/latest/graph_models.html) to create the database schema. In short it shows the relationships between the different models in the database connected to the application. Graph Models exports a *.dot file which easily can be converted to a more 'easy to read' design with the help of the application [dreampuf](https://dreampuf.github.io/GraphvizOnline/).

Models used (besides standard user model) in this project are:

* **Category** - Handles categories. I made a specific model to be able to add more dynamics (create / remove categories going forward in the admin backend instead of 'hard code' it in the code).
* **Genre** - Handles genres. I made a specific model to be able to add more dynamics (create / remove genres going forward in the admin backend instead of 'hard code' it in the code).
* **Post** - Handles all the reviews
* **Comment** - Handles all the comments
* **UserProfile** - Handles the user profile information (first name, last name, presentation and featured image for the specific user/reviewer). There is a one-to-one relation to the user model to connect it to the standard user model.

<details><summary><b>Database Schema</b></summary>

![Database Schema](readme/assets/images/database_schema.png)
</details><br/>

# **User Experience (UX)**

## Wireframes
The wireframes for the site were created in the software [Balsamiq](https://balsamiq.com). The wireframes have been created for desktop, tablet and mobile devices. The text content wasn't finalized during the wireframe process. It's worth mentioning that there are visual differences compared to the wireframes, the reason being design choices that was made during the creation process.

<details><summary><b>Wireframes</b></summary>

![Wireframes](readme/assets/images/balsamiq.png)
</details><br/>

## Design
### Flowchart:
![Flowchart](Documents/py.flowchart.png)
I used [Lucid](https://www.lucidchart.com/) to create a flowchart, to enhence the overall structure.

[Back to top](<#table-of-contents>)

## Features

### Existing Features:


[Back to top](https://github.com/Blog#1key-project-information)
  
---

# **. User Experience (UX)**

## **.1. The Strategy Plan**

### The Idea

**Just ask** Blog website is a question-and-answer website where users can ask questions, answer questions, and interact with other users by liking or dislinking comments. It covers a wide range of topics from technology and business to health and entertainment. Users can follow topics, answer questions based on their expertise, and engage in discussions with a community of users. Just Ask's objective is to connect people with information and allow them to share knowledge and learn from each other.
### The Ideal User
The target audience is anyone curouis of the outside world and is interested to interact with other people.

- User can `like` or `dislike`on posts
- User can comment
- User can `delete` or `edit` his/her posts

### **.1. Site Goals**

- Inform and Educate: Provide accurate and up-to-date information on baby care and parenting.
- Engage and Support: Create a community where parents can connect, share experiences, and offer mutual support.

### Epics

As a thought process of the strategy plane, 9 epics were created and utilized. Please see below the detail list of epics with links, or a link to the project's [Kanban Board](https://github.com/users/EIN-1/projects/5). Those Epics were further sliced into USER STORIES.

![Kanban Board](/image/userstories1.png)
![Kanban Board](/image/userstories2.png)

- [Epic 1: Environment Configuration](https://github.com/users/EIN-1/projects/5/views/1?pane=issue&itemId=70745632)
- [Epic 2: Database Models](https://github.com/users/EIN-1/projects/5/views/1?pane=issue&itemId=70745621)
- [Epic : Admin Panel](https://github.com/users/EIN-1/projects/5/views/1?pane=issue&itemId=70745627)
- [Epic 4: Post Views and likes](https://github.com/users/EIN-1/projects/5/views/1?pane=issue&itemId=70745630)
- [Epic 5: User Authentication](https://github.com/users/EIN-1/projects/5/views/1?pane=issue&itemId=70745637)
- [Epic 6: flowchart and design](https://github.com/users/EIN-1/projects/5/views/1?pane=issue&itemId=70745620)
- [Epic 7: Create search bar and button](https://github.com/users/EIN-1/projects/5/views/1?pane=issue&itemId=70745624)
- [Epic 9: Testing and Validation](https://github.com/users/EIN-1/projects/5/views/1?pane=issue&itemId=70745636)

### User stories

User stories were created based on the Epics. Each user story uses the MoSCoW prioritization technique. Each user story on the [Kanban Board](https://github.com/users/EIN-1/projects/5/views/1) was given (MoSCoW) labels.


#### MoSCoW prioritization technique stands for:

**Must-Have**: Critical requirements that must be implemented for the project to be considered successful.

**Should-Have**: Important requirements that are not critical but add significant value.

**Could-Haves**: Desirable features that would be nice to have but are not crucial.

**Won't-Have**: Features that are explicitly excluded from the project scope.


### List of user stories sorted by Epic :

## **.2. The Scope Plane**

After decided on the strategy, the scope plane was carefully created.

### .2.1. Features to be implemented

- **Search** : Search bar for guests and users is provided on landing page so users can find specific News Posts, Styles or Team members.
- **Comment**: Allow users to reply directly to another comment. Replies would then be shown directly underneath that comment as a conversation.

## **.. The Structure Plane**

### ..1. Site Maps

## Database Schemas

Following schema shows intended database structure:

![Database schema](/docs/dbase/schema.db.png)
- I designed my database for coding to stay in the line and to have a clear picture of my database.

## The Skeleton Plane


### Wire-frames
[wireframes](/docs/wireframes.png)

 I created simple ![wireframes](/docs/wireframes.png) for the homepage, and the article detail page. For the registration and login page I was planning to use the default layout, so I omitted wireframes for those pages.


## The Surface Plane

 ### Color pallette

 - Primary Color (#763ae0): This vibrant shade of purple is eye-catching and energetic, serving as the primary color to draw attention to important 
  elements on the website

 - Secondary Color (#a0d333): This soft green hue complements the primary color palette, bringing a refreshing and natural feel to the design

 - Background Color (#FFF5E1): This light cream or ivory tone provides a clean and neutral background for the website, ensuring readability and allowing   other colors to stand out effectively.

 - Text Dark (#333333): A dark gray color, perfect for body text or any content where readability is crucial.

- Text Light (#767268): A lighter shade of gray, suitable for secondary text or elements where a softer contrast is desired

### .5.. Fonts
[Google Fonts](https://fonts.google.com/) site was used to pick the best typography style. The most importance was given to balance between style and readability. As a developer I needed to ensure that all text is displayed clear.

### .5.4. Icons and pictures

# Features

 ## Features used in every HTML template

  ### Header
  ![header](/image/header.png)

  - It is fully responsive and includes the just ask blog name on the left and member links and blog slogan on the right.

  - The blog name is wrapped in a link and can be used to navigate to the homepage.

  - After logging in, the links on the right side are replaced by the Read Later and a log-out button.

  ### Footer
  ![footer](/image/footer.png)

  - Every page has a footer at the bottom of the page.
  - The footer shows the copyright text and links to four different social media websites. Each link opens in a new tab.

  ### Login
![login](/image/login-form.png)
- Every template in this project is equipped with Favicon. This is to ease navigation for user in case of more tabs opened. 
  ### Register
  ![register](/image/register-form.png)
  - Every template in this project is equipped with Favicon. This is to ease navigation for user in case of more tabs opened. 
  ### Reset password
  ![reset](/image/reset-password.png)
 - Every template in this project is equipped with Favicon. This is to ease navigation for user in case of more tabs opened. 
 ### Landing page
 ![landing page](/image/landing%20page.png)
 - Every template in this project is equipped with Favicon. This is to ease navigation for user in case of more tabs opened. 
 ### Profile
 ![profile](/image/user-profile.png)
 - Every template in this project is equipped with Favicon. This is to ease navigation for user in case of more tabs opened. 
 ### Search
 ![search](/image/search.png)
 - Every template in this project is equipped with Favicon. This is to ease navigation for user in case of more tabs opened. 
 ### Highlight post
 ![post](/image/highlight.png)
 - Every template in this project is equipped with Favicon. This is to ease navigation for user in case of more tabs opened. 
 ### Categories
 ![categories](/image/categories.png)
 - Every template in this project is equipped with Favicon. This is to ease navigation for user in case of more tabs opened. 
 ### Admin
 ![Superuser](/image/superuser.png)
 - Every template in this project is equipped with Favicon. This is to ease navigation for user in case of more tabs opened.
  #### Admin  for user in case of more tabs opened.

 
 ### Error Pages

 - This project is designed to have custom error pages. In case of user clicks on broken link, submits action that isn't supported or tries to reach certain view without permission, then user isn't completely "cut off" from browsing, instead an error page with header and footer appears and user is informed of the situation.

 The following custom error pages were created :

 - 403 - Received when user attempts to access a web resource for which they lack the necessary permissions. 
 - 404 - Encountered when the requested web resource by user is not found on the server. 
 - 500 - Displayed when the web server encounters an internal error while processing the request.

## Main Content

  ### Landing Page
  ![header](/image/header.png)
  - **Template File :** `home.html` - extends `base.html`
  - Contains list of posts.
  - Provides user with all Posts published along with name of creator, date created and a snippet of Post body. Also number of votes and comments is provided to both logged in and not logged in users 

  ### next Page

  - **Template File :** `post_detail.html` - extends `base.html`
  - **User :** Provides user with selected Post along with name of creator, date created and full Post body. User sees votes and amount of comments. Logged in user has ability to comment, delete and vote.

### **4.2.4. Read Later Page**

- **Template File :** `read_later.html` - extends `base.html`
- **User :** Enables logged in user to read bookmarked posts. If there is no bookmarked posts, 

### Forms

- **App :** `AllAuth` extension
- **Template File :** `*.html` in `./templates/account` - extends `base.html`
- **User :** Forms do interact with user. They are designed to be clear and to the point, always in center of the screen. 


# Validation, Testing & Bugs
## Testing

### Validator Testing
  #### PEP8 CI Validation
  ![PEP8 CI Validation](Documents/pep-validator.png)
  No errors were found in [CI PEP8 Online testing](https://pep8ci.herokuapp.com/).

  #### Lighthouse
  ![Lighthouse test](docs/testing/lighthouse3.png)
  In general it was working well with [Lighthouse testing](https://pep8ci.herokuapp.com/)

### Manual Testing
  #### Erroe message 
  ![Invalid Input ](Documents/invalid-input.png)
    Any input that is not a number from the given options is an error, the user will be prompted with an `error message` until the player enters the correct number.

  #### Invalid response
  ![Invalid choise at the end](Documents/yes-or-no.png)
  Any input other than a `yes or no` will be considered `invalid` at the end of the game, this is not case sensitive so it can be in lower or uppercase letters.

### Responsiveness Test
The responsive design tests were carried out manually with [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) and [Responsive Design Checker](https://www.responsivedesignchecker.com/).

| Desktop    | Display > 1280px      | Display < 1280px   |
|------------|-----------------------|--------------------|
| Render     | pass                  | pass               |
| Links      | pass                  | pass               |
| Images     | pass                  | pass               |

| Tablet     | Samsung Galaxy Tab 10 | Amazon Kindle Fire | iPad Mini | iPad Pro |
|------------|-----------------------|--------------------|-----------|----------|
| Render     | pass                  | pass               | pass      | pass     |
| Links      | pass                  | pass               | pass      | pass     |
| Images     | pass                  | pass               | pass      | pass     |

| Phone      |Galaxy S5/S6/S7/S20+   | iPhone 6/7/8/ plus | iPhone 14pro max     |
|------------|-----------------------|--------------------|----------------------|
| Render     | pass                  | pass               | pass      | pass     |
| Links      | pass                  | pass               | pass      | pass     |
| Images     | pass                  | pass               | pass      | pass     |

[Back to top](<#table-of-content>) 
### Browser Compatibility
`justask` blog was tested for functionality and appearance in the following browsers on desktop. No visible or funcional issues on all 
the browsers below.

- Google Chrome - Version 121.0.6422.114 (Official Build) (64-bit)
- Microsoft Edge - Version 124.0.2478.80 (Official build) (64-bit)
- Mozilla Firefox - 127.0 (64-bit)

[Back to top](<#table-of-content>)

### Bugs
- while loop was not exiting but it was an operander issue, it got fixed as for now no bugs

### Remaining Bugs
- No bugs remaining as far as I know.

[Back to top](<#table-of-contents>)

## Technologies Used
### Main Language
- Python Language

### Frameworks, Libraries & Programs
- [Lucid](https://www.lucidchart.com) - to create the mock-up in preparation for the project.
- [codeanywhere](https://code.visualstudio.com/) - used as the coding environment.
- [GitHub](https://github.com/) - to store the repository for submission.
- [Heroku](https://id.heroku.com/) - to deploy the live version of the terminal.
- [AmIResponsive](https://ui.dev/amiresponsive?url=https://hangmangame-pp3-python-d5764adc1207.herokuapp.com/) - the responsive preview image on different gadgets.
- [iloveimg](https://www.iloveimg.com/) - to compress the images.
- Colorama - to add colored text to improve the readability by adding a color to the print statements and improve the user experience.
- pyfiglet - to add ASCII font text in the game to improve the user experience.
- pycountry - to add all the country names for the user to type in his country location.

[Back to top](<#table-of-contents>)

## Deployment
  ### Version Control
  The version control was maintained using git within Codeanywhere to push code to the main repository.

  * From the codeanywhere terminal type `"git add ."`, to make changes and/or updates to the files.

  * Type `"git commit -m (insert a short descriptive text)"`, which commits the changes and updates the files.

  * Use the `"git push"` command, which pushes the committed changes to the main repository. 

  ### Page Deployment
  The app was deployed to Heroku CLI. The steps to deploy are as follows:

  * After creating an account and logging in, click `"creat new"` to create a new app from the dashboard.
  * Create a unique name for the app and select my region; press `"Create app"`.
  * When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:
      1. `heroku/python`
      2. `heroku/nodejs`
  * Go to `"Settings"` and navigate to `Config Vars`.
  * Add Config Var. 
    * For this app I only used: `KEY` = `PORT` : `VALUE` = `8000`.
  * Add buildpacks `Python` and `NodeJS` - in this order.
  * Click the `Deploy Branch`.
  * Scroll Down to Deployment Method and select GitHub.
  * Select the repository to be deployed and connect to Heroku.
  * Scroll down to deploy: 
      * at first I used`Option 2` it selects manually deploys (Will Update manually with every "git push"). To see my progress and changes.
      * at the end I used `Option 1` it selects Automatic deploys (Will Update automatically with every "git push"). This was chosen for this project.
  * Live deployment [Python quiz](https://python-quiz-da8ccddf3267.herokuapp.com/)

  [Back to top](<#table-of-contents>)
## Fork
  ### How To Fork The Repository On GitHub
  ![Fork](Documents/fork.png)
  It is possible to do a copy of a GitHub Repository by forking the GitHub account. The copy can then be viewed and it is also possible to do changes in the copy without affecting the original repository. To fork the repository, take these steps:

  1. After logging in to GitHub, locate the repository. On the top right side of the page there is a 'Fork' button. Click on the button to create a copy of the original repository.

  [Back to top](<#table-of-content>)

## Clone
  ### Create A Local Clone of A Project
  ![Clone](Documents/clone.png)
  To create a local clone of your repository, follow these steps:

  1. When you are in the repository, find the code tab and click it.
  2. To the left of the green GitPod button, press the 'code' menu. There you will find a link to the repository. Click on the clipboard icon to copy the URL.
  . Use an IDE and open Git Bash. Change directory to the location where you want the cloned directory to be made.
  4. Type 'git clone', and then paste the URL that you copied from GitHub. Press enter and a local clone will be created.

  [Back to top](<#table-of-content>)


## Credits
For inspiration, I watched the following YouTube tutorials by:
- [Bro code](https://www.youtube.com/watch?v=zehwgTB0vV8) -Python quiz game
- [Kite](https://www.youtube.com/watch?v=m4nEnsavl6w&t=3s)
- [Colored Console Output in Python](https://www.youtube.com/watch?v=kf8kbUKeM5g) - to learn how to use colorama in the print statements to enhance the overall user experience.
- [Bytive](https://www.youtube.com/watch?v=NLqSxyKh1EU) - How to measure elapsed time in Python.
- [Learn Learn Scratch Tutorials](https://www.youtube.com/watch?v=U1aUteSg2a4) - Python - Converting text to Big ASCII Text using Pyfiglet.

To understand and implement the logic required for the game the following pages were consulted:
+ [Brock Byrd](https://brockbyrdd.medium.com/creating-a-multiple-choice-quiz-in-python-terminal-1c46123b86d5) -Creating a multiple choice quiz in Python.
+ [some quiz quetions](https://www.w3schools.com/quiztest/quiztest.asp?qtest=PYTHON) - question ideas.
+ [Change the color of text in python shell?](https://stackoverflow.com/questions/11043260/change-the-color-of-text-in-python-shell) - to print different colored text.
+ [How to make colored text in python by MiloCat](https://ask.replit.com/t/how-do-i-make-colored-text-in-python/29288/8) - to display the text in different colors.
+ [Timer](https://www.learndatasci.com/solutions/python-timer/) - as a reference how to add the execution time before the game begins. 
+ [codedamn](https://codedamn.com/news/python/strip-whitespace-in-python) - Python Strip Whitespace: A Complete Guide
+ [stack overflow](https://stackoverflow.com/questions/51804117/conditions-are-met-but-program-not-breaking-out-of-while-loop) - conditions are met, but program not breaking out of while loop 

[Back to top](<#table-of-contents>)

  #### Admin comment
  ![Admin comment](/image/superuser-add-comment.png)
  - Every template in this project is equipped with Favicon. This is to ease navigation for user in case of more tabs opened.
  #### Admin delete
  ![Admin delete](/image/superuser-delete.png)
  - Every template in this project is equipped with Favicon. This is to ease navigation for user in case of more tabs opened.
  #### Admin reation
  ![Admin reation](/image/superuser-reaction2.png)
  - Every template in this project is equipped with Favicon. This is to ease navigation

[Back to top](<#table-of-content>)

## Validation

Validation will be here [validation.md](/docs/validation.md) file.

[Back to top](<#table-of-content>)

## Testing

-Tested for responsiveness manually.
![lighthouse testing](/docs/testing/lighthouse3.png) 
-I used lighthouse testing for my page

[Back to top](<#table-of-content>)

## Bugs

- [** Stackoverflow Django annotate() multiple times causes wrong answers **] (https://stackoverflow.com/questions/1265190/django-annotate-multiple-times-causes-wrong-answers) - It helped in fixing bug with likes and dislikes showing wrong counts by adding distinct=True in my multiple annotation in the home view see below
![fixed bug](image.png)

[Back to top](<#table-of-content>)

# Deployment**

## Transfer of progress from IDE**

- **Task :** To ensure regular commitments are done to avoid any data/progress loss.
- **Method :** 
   - commands `git add [filename]` was used to add specific file to staging area, alternatively command `git add .` was used to add all changed files to staging area
   - command `git commit -m "[commit description]"` was used to add commitments into queue
   - command `git push` was used to push all commitments to remote repository on GitHub

## Offline cloning

  - **Task :** To use repository on local machine.
  - **Method :** 
  - Navigate to GitHub and follow `Code -> HTTPS -> Copy button` . after those steps open your local coding environment and type `git clone [copied link]`.

## Deployment Prerequisites**

  ### Gmail

  - **Task :** Obtain GMail username and app key (password) - GMAIL SMTP to be used as mailing client.
  - **Method :** 
    - Navigate to `https://accounts.google.com/` and follow all steps for registering new email address
    - Login to google with newly created email address and password.
    - Navigate to `https://accounts.google.com/` once again
    - Select `Security > Signing in to Google > 2-Step Verification > App Passwords`
    - Enter a name of the app password and select `Generate`
    - You will get app password in format `xxxx xxxx xxxx xxxx`
    - Update `settings.py` in the project directory

  ### PostgreSQL

  - **Task :** Obtain database URL to be used as project's database.
  - **Method :** 
    - Select one of the DB providers, I did use [PostgreSQL](https://www.postgresql.org/) which I received from Code institute per resquest.
    
    below will be deleted
    - Navigate to `https://dbs.ci-dbs.net/` and follow all steps for registering new account
    - Login to CI DB with newly created account credentials
    - Navigate to `+ Create New Instance`
    - Select `Name, Plan and Region`
    - Confirm the instance by pressing `Create Instance`
    - Obtain database URL in format 
    - Update `settings.py` in the project directory

  ### Cloudinary

  - **Task :** Obtain Cloudinary URL to be used as project's static storage
  - **Method :** 
    - Select one of the static storage providers, I did use [Cloudinary](https://console.cloudinary.com/)
    - Navigate to `https://console.cloudinary.com/` and follow all steps for registering new account
    - Login to Cloudinary with newly created account credentials
    - Navigate to `+ Add a new environment`
    - Confirm your selection
    - Obtain Cloudinary URL in format `cloudinary://USER:PASSKEY@ENVIRONMENT`
    - Update `settings.py` in the project directory

  ### Settings.py & file-tree**

  - **Task :** Prepare `settings.py` adn file-tree for deployment 
  - **Method :** 
    - Create file `env.py` to keep all sensitive information in
    - See example of `env.py` file *( Appendix 48 )*
    - Add `env.py` into `.gitignore` file to ensure this fill won't be uploaded to GitHub
    - update `settings.py` with `import os`
    - for every secured variable add code `VARIABLE = os.environ.get("VARIABLE")`
    - ensure this process for Gmail, ElephantSQL, Cloudinary, DEBUG and Django Secret Key
    - update default database settings in `settings.py` with `
  if "DATABASE_URL" in os.environ:
      DATABASES = {"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))}
  else:
      DATABASES = {
          "default": {
              "ENGINE": "django.db.backends.sqlite3",
              "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
          }
      }`
    - update default static settings in `settings.py` with `
    STATIC_URL = "/static/"
  STATICFILES_STORAGE = "cloudinary_storage.storage.StaticHashedCloudinaryStorage"
  STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
  STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
  CLOUDINARY_URL = os.environ.get("CLOUDINARY_URL")
  MEDIA = "/media/"
  DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
    `
    - update email settings in `settings.py` with `EMAIL_HOST = "smtp.gmail.com"
  EMAIL_PORT = 587
  EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
  EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
  EMAIL_USE_TLS = True`
    - Migrate - your database models to Database using `python manage.py migrate` command
    - Create directories `.\static` and `.\templates`
    - commit and push changes to GitHub 


[Back to top](<#table-of-content>)

  ### Deployment to Heroku**

- **Task :** To ensure users are able to view live version of **Aneta's Glimmer** project.
- **Method :** 
  - Register & Log In with heroku
  - Navigate to `New > Create New App`
  - Select Name of the app that is unique
  - Navigate to `Settings > Reveal Config Vars`
  - Add all variables from `env.py` to ConfigVars of Heroku App 
  - Add variable pair `PORT:5000`
  - For the testing deployment add variable pair `COLLECT_STATIC:1`
  - Add the Heroku app URL into `ALLOWED HOSTS` in `settings.py`
  - In root create file name `Procfile`
  - Navigate to `Deploy > GitHub > Connect`
  - Navigate to `Deploy > Deploy Branch`
  - Optionally, you can enable automatic deploys
  - See the deployment log - if the deployment was successful, you will be prompted with option to see live page  

## Technologies & Credits**

### Technologies used to develop and deploy this project

- [**Balsamiq**](https://balsamiq.com/support/) - to create wireframes.
- [**Schemas**](https://app.diagrams.net/) - to create database structure.

- [**Django/Jinja**](https://docs.djangoproject.com/en/5.0/) - main Framework of the project
- [**Python**](https://www.python.org/) - main BackEnd programming language of the project
- [**HTML**](https://developer.mozilla.org/en-US/docs/Web/HTML) - templates programming language of this project (FrontEnd)
- [**CSS**](https://developer.mozilla.org/en-US/docs/Web/CSS) - styling the project via external CSS file `./static/css/style.css`
- [**Java Script**](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - dynamic templates programming language of this project (FrontEnd)
- [**jQuery**](https://api.jquery.com/) - API for JavaScript - dynamic templates programming language of this project (FrontEnd)
- [**Bootstrap v. 5.**](https://getbootstrap.com/) - styling framework used in this project (FrontEnd)

- [**Gitpod**](https://gitpod.com/) - online IDE - gitpod was used to create this project
- [**Git**](https://git-scm.com/doc) - to make commitments of progress and push the results back to GitHub
- [**GitHub**](https://github.com/) - to keep the track of version control
- [**Heroku**](https://heroku.com) - to deploy this project

- [**Google Fonts**](https://fonts.google.com/) - used for picking the best typography
- [**PostgresSQL**](https://www.postgressql.com/) - used as a database storage
- [**Cloudinary**](https://console.cloudinary.com/) - used as a storage of static files
- [**FavIcon.io**](https://favicon.io/favicon-converter/) - used to compress favicon
- [**W3Schools**](https://www.w3schools.com/) - useful information and cheat sheets

[Back to top](<#table-of-content>)


### Requirements.txt
- Before running the system install all requirements by running the command below
  `pip install -r requirments.txt` 
    asgiref==.8.1
    dj-database-url==0.5.0
    Django==4.2.13
    django-bootstrap-v5==1.0.11
    django-fontawesome-5==1.0.18
    django-gravatar2==1.4.4
    django-static-jquery==2.1.4
    Faker==26.0.0
    gunicorn==22.0.0
    psycopg2==2.9.9
    python-decouple==.8
    sqlparse==0.5.0
    whitenoise==6.7.0

- following commands to set environment variables in developement:
  Press enter after every export command
    `export DEBUG=True`
    `export SECRET_KEY='random_striing'`
    `export DATABASE_URL='my postgreSQL datbase'`
  Then `python manage.py runserver` to go to the browser.

[Back to top](<#table-of-content>)

### Credits
-this might change!!!!
- [**The Django admin site**](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/) - How to set up my Superuser Admin.
- [**jQuery.post()**](https://api.jquery.com/jQuery.post/)
- [**Django documentation template comments**](https://docs.djangoproject.com/en/5.0/ref/templates/language/#comments) - Setting up my comments template 
- [**django-gravatar**](https://github.com/twaddington/django-gravatar) - How to use gravatar icons on my blog.
- [**Geeksforgeeks Django Jinja**] (https://www.geeksforgeeks.org/jinja-for-server-side-rendering-in-django/) - How to work with jinja.
- [**Django Templates**] (https://docs.djangoproject.com/fr/4.2/topics/templates/) - How to work with templates.
- [**Django documentation Model.__str__**] (https://docs.djangoproject.com/en/5.0/ref/models/instances/) - How to work with model string.
- [**Stackoverflow How to set up Django website with jQuery**] (https://stackoverflow.com/questions/12031825/how-to-set-up-django-website-with-jquery)

[Back to top](<#table-of-contents>)

 ## Acknowledgments
 The application `Python quiz` was completed as the Portfolio Project  (*Python*) for the Full Stack Software Development Diploma at the [Code Institute](https://codeinstitute.net/).
  - A special thanks to my cohort facilitator `Ms. Kay Welfare` for her advice and support her quick feedback was very helpful and encouraging.
  - I would like to thank my mentor Mr. [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/) for relevant feedback during the project.
  
 - **Developer :** [Elsie Nagawa ](https://github.com/EIN-1/justask)
 19.07.2024.

 [Back to top](<#table-of-contents>)