# Introduction


### Project Goals

# Table of contents

- [User Stories](#user-stories)
    - [Developer](#developer)
    - [User/shopper](#usershopper)
- [Design](#design)
    - [Look and feel](#look-and-feel)
    - [Colour](#colour)
    - [Typography](#typography)
    - [Wireframes](#wireframes)
      - [Home Page desktop Wireframe](#home-page-desktop-wireframe)
      - [Home Page mobile Wireframe](#home-page-mobile-wireframe)
- [Database Schemas](#database-schemas)
    - [User model](#user-model)
    - [UserProfile model - users app](#userprofile-model---users-app)
    - [Meme model - memes app](#meme-model---memes-app)
    - [Comment model - memes app](#comment-model---memes-app)
    - [Tag model - memes app](#tag-model---memes-app)
    - [ContactForm model - memes app](#contactform-model---memes-app)
- [Agile Development](#agile-development)
- [Tools and technologies used](#tools-and-technologies-used)
    - [Languages and Frameworks](#languages-and-frameworks)
    - [Django Packages](#django-packages)
    - [Other tools and programs.](#other-tools-and-programs)
- [Features](#features)
    - [Home Page](#home-page)
    - [Memes Page](#memes-page)
    - [Delete Meme Confirmation Page](#delete-meme-confirmation-page)
    - [Single Meme Page](#single-meme-page)
    - [Report Meme Page](#report-meme-page)
    - [Users Page](#users-page)
    - [Single User Page](#single-user-page)
    - [Edit Profile Page](#edit-profile-page)
    - [Delete Profile Confirmation Page](#delete-profile-confirmation-page)
    - [Upload Meme / Edit Meme Page](#upload-meme--edit-meme-page)
    - [Login Page](#login-page)
    - [Password Reset Page](#password-reset-page)
    - [Logout Page](#logout-page)
    - [Sign-up Page](#sign-up-page)
    - [Contact Developer Page](#contact-developer-page)
    - [Custom Error 404 Page](#custom-error-404-page)
    - [Custom Error 500 Page](#custom-error-500-page)
  - [Features Left to Implement](#features-left-to-implement)
- [Testing](#testing)
  - [Code Validation](#code-validation)
    - [Google lighthouse Validation](#google-lighthouse-validation)
    - [CSS Validation](#css-validation)
    - [HTML Validation](#html-validation)
    - [JavaScript Validation](#javascript-validation)
    - [PEP8 Code Institute Python Linter Validation](#pep8-code-institute-python-linter-validation)
      - [Techmeme project app](#techmeme-project-app)
      - [memes app](#memes-app)
      - [users app](#users-app)
- [Manual Testing](#manual-testing)
    - [Devices and browsers used for testing](#devices-and-browsers-used-for-testing)
    - [User Stories Testing](#user-stories-testing)
    - [Home Page Testing.](#home-page-testing)
    - [Memes Page Testing.](#memes-page-testing)
    - [Single Meme Page Testing.](#single-meme-page-testing)
        - [Authenticated user and owner of the meme.](#authenticated-user-and-owner-of-the-meme)
        - [Authenticated user and not the owner of the meme.](#authenticated-user-and-not-the-owner-of-the-meme)
        - [Not authenticated user.](#not-authenticated-user)
    - [Users Page Testing.](#users-page-testing)
    - [Single User Page Testing.](#single-user-page-testing)
        - [Authenticated user and owner of the profile.](#authenticated-user-and-owner-of-the-profile)
        - [Not authenticated user.](#not-authenticated-user)
    - [Upload Meme Page Testing.](#upload-meme-page-testing)
        - [Not authenticated user.](#not-authenticated-user)
        - [Authenticated user.](#authenticated-user)
    - [Contact Developer Form Testing.](#contact-developer-form-testing)
        - [Not authenticated user.](#not-authenticated-user)
        - [Authenticated user.](#authenticated-user)
    - [Update Meme Form Page Testing.](#update-meme-form-page-testing)
    - [Delete Confirmation Page Testing.](#delete-confirmation-page-testing)
    - [Logout Page Testing.](#logout-page-testing)
    - [Login Page Testing.](#login-page-testing)
    - [Home Page Testing.](#home-page-testing)
    - [Password Reset Page Testing.](#password-reset-page-testing)
    - [Sign Up Page Testing.](#sign-up-page-testing)
  - [Interesting bugs or problems](#interesting-bugs-or-problems)
  - [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
    - [Deploy with Heroku](#deploy-with-heroku)
    - [Clone project](#clone-project)
    - [Fork repository](#fork-repository)
- [Content](#content)
- [Credits](#credits)

# User Stories


### Developer
1. As a developer I can use local IDE to develop the project.
2. As a developer I can deploy the project to Heroku early in the development process.
3. As a developer I can create wireframes for the project so that I have a clear idea of what I want to achieve.
4. As a developer I can create a database schema for the project so that I have a clear idea of what models I need to create.


### User/shopper
1. As a user I want to be able to view the site on any device I choose.
2. As a user I want to be able to create an account.
3. As a user I want to be able to log in and out of my account.
4. As a user I want to be able to reset my password if I forget it.
5. As a user I want to be able to find the products I am looking for easily.
6. As a user I want to be able to view the details of a product.
7. As a user I want to be able to add a product to my shopping bag.
8. As a user I want to be able to edit the quantity of a product in my shopping bag.
9. As a user I want to be able to delete a product from my shopping bag.
10. As a user I want to be able to view my shopping bag.
11. As a user I want to be able to checkout securely.
12. As a user I want to be able to view my order history.
13. As a user I want to be able to leave a review for a product.
14. As a user I want to be able to view other users reviews.
15. As a user I want to be able to edit my reviews.
16. As a user I want to be able to delete my reviews.
17. As a user I want to be able to search for a product by name or description.
18. As a user I want to be able to add a product to the favorites list.
19. As a user I want to be able to view my favorites list.
20. As a user I want to be able to remove a product from my favorites list.


# Design

### Look and feel


### Colour


### Typography


### Wireframes

#### Home Page desktop Wireframe

![Home Page Wireframe](/static/images/readme_images/wireframes/home_desktop.png)

#### Home Page mobile Wireframe

![Home Page Wireframe](/static/images/readme_images/wireframes/home_mobile.png)

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
