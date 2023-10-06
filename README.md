# Introduction




### Project Goals

# User Stories

### Developer
As a developer

### First Time Visitor Goals



### Authenticated User Goals



### Site owner objectives

# Design

### Look and feel


### Colour


### Typography


### Wireframes

#### Desktop Wireframe


#### Mobile Wireframe

# Database Schemas


### User model



### UserProfile model - users app



### Meme model - memes app


### Comment model - memes app



### Tag model - memes app


### ContactForm model - memes app



# Agile Development



# Tools and technologies used

### Languages and Frameworks

### Django Packages


### Other tools and programs.



# Features



### Home Page

### Memes Page

### Delete Meme Confirmation Page

### Single Meme Page


### Report Meme Page


### Users Page 


### Single User Page


### Edit Profile Page


### Delete Profile Confirmation Page

### Upload Meme / Edit Meme Page

### Login Page


### Password Reset Page


### Logout Page


### Sign-up Page

### Contact Developer Page


### Custom Error 404 Page


### Custom Error 500 Page



## Features Left to Implement


# Testing

## Code Validation

### Google lighthouse Validation



### CSS Validation

### HTML Validation


### JavaScript Validation


### PEP8 Code Institute Python Linter Validation



#### Techmeme project app

#### memes app



#### users app



 # Manual Testing

### Devices and browsers used for testing


### User Stories Testing




### Home Page Testing.



### Memes Page Testing.



### Single Meme Page Testing.

- The Navigation bar and footer are the same as on the home page.

##### Authenticated user and owner of the meme.

##### Authenticated user and not the owner of the meme.

##### Not authenticated user.

### Users Page Testing.


### Single User Page Testing.


##### Authenticated user and owner of the profile.

##### Not authenticated user.

### Upload Meme Page Testing.

##### Not authenticated user.

##### Authenticated user.

### Contact Developer Form Testing.

##### Not authenticated user.


##### Authenticated user.

### Update Meme Form Page Testing.


### Delete Confirmation Page Testing.


### Logout Page Testing.


### Login Page Testing.


### Home Page Testing.

### Password Reset Page Testing.


### Sign Up Page Testing.


## Interesting bugs or problems


## Unfixed Bugs


# Deployment

### Deploy with Heroku

1. Go on to [Heroku](https://www.heroku.com/) website and [log in](https://id.heroku.com/login) if you already have an account or [sign up](https://signup.heroku.com/) if you don't. 
2. Click on the "New" button on the top right of the home page and select "Create new App" from the drop-down menu.
3. In the "App name" field enter the name of your app. This name has to be unique. 
    - Heroku displays a green tick if your app name is available.
4. In the "Choose a region" field choose either the United States or Europe based on your location.
5. Click the "Create app" button.
6. Next page, top centre of the screen, select the "Settings" tab. 
7. In the "Config Vars" section, click on the "Reveal config Vars" button.
8. In this section you need to enter your environment variables. Usually stored in the env.py file locally. In my case, I have 10 variables: 
    - SECRET_KEY - Django secret key.
    - AWS_ACCESS_KEY_ID - Amazon AWS access key.
    - AWS_SECRET_ACCESS_KEY - Amazon AWS secret access key.
    - AWS_STORAGE_BUCKET_NAME - Amazon AWS bucket name.
    - DATABASE_USER - Amazon RDS database user.
    - EMAIL_HOST_PASS - Email password.
    - EMAIL_HOST_USER - Email address.
    - DATABASE_HOST - Amazon RDS database host.
    - DATABASE_NAME - Amazon RDS database name.
    - DATABASE_PASS - Amazon RDS database password.
9. Copy and paste these variables into the KEY field and their values into the VALUE field.
10. Go back to the top of the screen and select the "Deploy" tab.
11. In the "Deployment method" section select "GitHub".
    1. In "Connect to GitHub" click on the "Search" button. Find the project repository in the list and click on the "Connect" button.
    2. Scroll to the bottom of that page. Click on the "Deploy Branch" button to deploy.
    3. You should also see an option to enable automatic deployment. If you enable this, every time you push to GitHub, Heroku will automatically deploy the app.
12. You will see build log scrolling at the bottom of the screen after that. When successfully finished building the app, you should see the link to your app.

NB: You will need to add your Heroku app link to the ALLOWED_HOSTS in the settings.py file. You also need to make sure that DEBUG is set to False, requirements.txt and Procfile are up to date and pushed to GitHub.


### Clone project 

- To clone this project.  
    - On my [GitHub](https://github.com/Inc21) profile page, top centre of the screen click on "repositories".
    -  Find and click on the "TechieMeme-PP4" repository.
    - In the repository page that opens, click on the 'Code' button.
    - Menu that opens make sure you are in the "local" tab, copy the link in "HTTPS".
    - paste that link into the relevant section in your ide to clone the repository.
        - CodeAnywhere. 
        - - Click on the "New Workspace" and paste that link to the "Repository URL" field.
        - vsCode. 
        - - Select "File" and "New Window". In the middle of the page select "Clone Git Repository...", 
        - - Paste that link into the search box at the top of the screen and hit enter.
        - - Select the local destination for repository files.
        

### Fork repository

- To fork this repository.
    - Open my [GitHub repository](https://github.com/Inc21/TechieMeme-PP4).
    - Click on the 'Fork' button on the top right of the screen.
    - On the 'Create a new fork' page you are given the option to rename that repository and then click on the green 'Create fork' button at the bottom of the form.


# Content


# Credits
