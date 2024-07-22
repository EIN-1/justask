![logo](static/img/justask.png)


# ***JustAsk Blog - Project Portfolio 4***
![am responsive](image/amResponsive.png)
# **1. Key project information**

- **Description :** **Just ask** is a question-and-answer website where users can ask questions, answer questions, and interact with other users.
- **Key project goal :** To familiarize visitors of this page with **justask** blog
- **Audience :** Target audience are users that are using search engines to ask quetions and those who are looking for answers from various topics
- **Live version :** Live version of **Just Ask** page can be viewed at [JustAsk](https://just-ask-b3c36fe12bcc.herokuapp.com/).

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
  +
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

## Project Management

### Kanban Board & User Stories
I've been using the application ``Kanban Board`` and the project board in GitHub to keep my project together. It has been working really well and has helped me structure up my work a lot. Trello was used on a more general plan and GitHub was used to plan and organize my user stories.

![Kanban Board](image/userstories1.png)


[Back to top](<#table-of-content>)

### Database Schema
I have used a modelling tool called [Graph Models](https://django-extensions.readthedocs.io/en/latest/graph_models.html) to create the database schema. In short it shows the relationships between the different models in the database connected to the application. Graph Models exports a *.dot file which easily can be converted to a more 'easy to read' design with the help of the application [dreampuf](https://dreampuf.github.io/GraphvizOnline/).

Models used (besides standard user model) in this project are:

* **Category** - Handles categories. I made a specific model to be able to add more dynamics (create / remove categories going forward in the admin backend instead of 'hard code' it in the code).
* **Genre** - Handles genres. I made a specific model to be able to add more dynamics (create / remove genres going forward in the admin backend instead of 'hard code' it in the code).
* **Post** - Handles all the reviews
* **Comment** - Handles all the comments
* **UserProfile** - Handles the user profile information (first name, last name, presentation and featured image for the specific user/reviewer). There is a one-to-one relation to the user model to connect it to the standard user model.

![Database Schema](docs/dbase/schema.db.png)

[Back to top](<#table-of-contents>)

## Features

### Existing Features:

[Back to top](https://github.com/Blog#1key-project-information)

### The Idea

**Just ask** Blog website is a question-and-answer website where users can ask questions, answer questions, and interact with other users by liking or dislinking comments. It covers a wide range of topics from technology and business to health and entertainment. Users can follow topics, answer questions based on their expertise, and engage in discussions with a community of users. Just Ask's objective is to connect people with information and allow them to share knowledge and learn from each other.
### The Ideal User
The target audience is anyone curouis of the outside world and is interested to interact with other people.

- User can `like` or `dislike`on posts
- User can comment
- User can `delete` or `edit` his/her posts

### Site Goals

- Share knowledge and experiences with the globle communty and to offer mutual support to one another.

### Epics

As a thought process of the strategy plane, 9 epics were created and utilized. Please see below the detail list of epics with links, or a link to the project's [Kanban Board](https://github.com/users/EIN-1/projects/5). Those Epics were further sliced into USER STORIES.

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

## The Scope Plane

After decided on the strategy, the scope plane was carefully created.

### Features 

- **Search** : Search bar for guests and users is provided on landing page so users can find specific News Posts, Styles or Team members.
- **Comment**: Allow users to reply directly to another comment. Replies would then be shown directly underneath that comment as a conversation.

[Back to top](https://github.com/Blog#1key-project-information)

## The Surface Plane

 ### Color pallette
- I used primary, success, light, dark for my webpage as they are the defaults of bootstrap.

  + dark = black
  + primary = blue
  + success = green
  + light = smoke white

## Features used 

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
 ![Superuser](/image/Admin.png)
 - Every template in this project is equipped with Favicon. This is to ease navigation for user in case of more tabs opened.
  #### Admin  for user in case of more tabs opened.

 
 ### Error Pages

 - This project is designed to have custom error pages. In case of user clicks on broken link, submits action that isn't supported or tries to reach certain view without permission, then user isn't completely "cut off" from browsing, instead an error page with header and footer appears and user is informed of the situation.

 The following custom error pages were created :

 ![Error 404](/image/noQuetionFound.png)
 - 404 - Encountered when the requested web resource by user is not found on the server. 
  ![Error 500](/image/warning.png)
 - 500 - Displayed when the web server encounters an internal error while processing the reques then it sends you a warning.


## Main Content

  ### Landing Page
  ![header](/image/main.png)
  - **Template File :** `home.html` - extends `base.html`
  - Contains list of posts.
  - Provides user with all Posts published along with name of creator, date created and a snippet of Post body. Also number of votes and comments is provided to both logged in and not logged in users.

### Forms

- **App :** `AllAuth` extension
- **Template File :** `*.html` in `./templates/account` - extends `base.html`
- **User :** Forms do interact with user. They are designed to be clear and to the point, always in center of the screen. 


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

- [**AmIResponsive**](https://ui.dev/amiresponsive) - the responsive preview image on different gadgets.
- [**iloveimg**](https://www.iloveimg.com/) - to compress the images.
- [**Google Fonts**](https://fonts.google.com/) site was used to pick the best typography style. The most importance was given to balance between style and readability. As a developer I needed to ensure that all text is displayed clear.
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
- [**Google Fonts**](https://fonts.google.com/) site was used to pick the best typography style. The most importance was given to balance between style and readability. As a developer I needed to ensure that all text is displayed clear.


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

  [Back to top](<#table-of-content>)




## Validation

[html validator](docs/testing/html-validator.png)
- The 3 errors could be fixed by changes the id names in each form but my time runout so i plan to fix the future.

[css validator](docs/testing/css.Validator.png)
- The warming are coming from the Django librarries, I was looking through them but they are almost the same dublicated warnings, I look forward in digging more into them when I have more time.

[Back to top](<#table-of-content>)

## Testing
- I used lighthouse testing and these are the results for desktop 
  ![lighthouse testing](/docs/testing/lighthousePC.png) 

- I used lighthouse testing and these are the results for mobile devices
   ![lighthouse testing](/docs/testing/lighthousePhone.png) 

- Tested for responsiveness manually and it was responding well.

[Back to top](<#table-of-content>)

## Bugs
- wrong count in likes, dislikes and comments but got fixed

- [**Stackoverflow Django annotate() multiple times causes wrong answers**] (https://stackoverflow.com/questions/1265190/django-annotate-multiple-times-causes-wrong-answers) - It helped in fixing bug with likes and dislikes showing wrong counts by adding distinct=True in my multiple annotation in the home view see below
![fixed bug](image will be put here.png)

[Back to top](<#table-of-content>)

# Deployment**

## Transfer of progress from IDE

- **Task :** To ensure regular commitments are done to avoid any data/progress loss.
- **Method :** 
   - commands `git add [filename]` was used to add specific file to staging area, alternatively command `git add .` was used to add all changed files to staging area
   - command `git commit -m "[commit description]"` was used to add commitments into queue
   - command `git push` was used to push all commitments to remote repository on GitHub

## Fork
  ### How To Fork The Repository On GitHub

  It is possible to do a copy of a GitHub Repository by ``forking the GitHub account``. The copy can then be viewed and it is also possible to do changes in the copy without affecting the original repository. To fork the repository, take these steps:

  1. After ``logging in to GitHub``, locate the ``repository``. On the ``top right side`` of the page there is a ``'Fork' button``. Click on the button to ``create a copy`` of the original repository.

## Clone
  ### Create A Local Clone of A Project
  
  To create a local clone of your repository, follow these steps:

  1. When you are in the repository, find the ``code tab`` and click it.
  2. To the ``left of the green GitPod button``, press the ``'code' menu``. There you will find a link to the repository. Click on the ``clipboard icon`` to copy the URL.
  Use an IDE and ``open Git Bash``. Change directory to the location where you want the cloned directory to be made.
  4. Type ``git clone``, and then ``paste the URL that you copied`` from GitHub. Press enter and a local clone will be created.

  [Back to top](<#table-of-content>)

## Offline cloning

  - **Task :** To use repository on local machine.
  - **Method :** 
  - Navigate to GitHub and follow `Code -> HTTPS -> Copy button` . after those steps open your local coding environment and type `git clone [copied link]`.

## Deployment Prerequisites

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

  ### Settings.py & file-tree

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

  ### Deployment to Heroku

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

- [**The Django admin site**](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/) - How to set up my Superuser Admin.
- [**jQuery.post()**](https://api.jquery.com/jQuery.post/)
- [**Django documentation template comments**](https://docs.djangoproject.com/en/5.0/ref/templates/language/#comments) - Setting up my comments template 
- [**django-gravatar**](https://github.com/twaddington/django-gravatar) - How to use gravatar icons on my blog.
- [**Geeksforgeeks Django Jinja**](https://www.geeksforgeeks.org/jinja-for-server-side-rendering-in-django/) - How to work with jinja.
- [**Django Templates**](https://docs.djangoproject.com/fr/4.2/topics/templates/) - How to work with templates.
- [**Django documentation Model.__str__**](https://docs.djangoproject.com/en/5.0/ref/models/instances/) - How to work with model string.
- [**Stackoverflow How to set up Django website with jQuery**](https://stackoverflow.com/questions/12031825/how-to-set-up-django-website-with-jquery)
- [**color testing**](https://color.a11y.com/Contrast/) - Checked my website color contex
- [**Password validation**](https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators) - with Django
- [**time zone**](https://docs.djangoproject.com/en/5.0/topics/i18n/) - Internationalization
- [**user authentication and management**](https://youtu.be/WuyKxdLcw3w?si=a_-3HyADtu5sblOR) - user authentication and management
- [**Ajax forn submission**](https://youtu.be/KgnPSmrQrXI?si=Y1Whk2AATEYZB1Dz) - Ajax forn submission


[Back to top](<#table-of-contents>)

 ## Acknowledgments
 The application `Just Ask` was completed as the Portfolio Project 4 for the Full Stack Software Development Diploma at the [Code Institute](https://codeinstitute.net/).
  - A special thanks to my cohort facilitator `Ms. Kay Welfare` for her advice and support her quick feedback was very helpful and encouraging.
  - I would like to thank my mentor` Mr. Precious Ijege` for relevant feedback during the project.
  
 - **Developer :** [Elsie Nagawa ](https://github.com/EIN-1/justask)
 22.07.2024.

 [Back to top](<#table-of-contents>)