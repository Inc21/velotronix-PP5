![VeloTronix Logo](/static/images/readme_images/velotronix_logo.png)
![mockup](/static/images/readme_images/mockup.png)

# Introduction
Velotronix is a fictional e-commerce website created for my fifth portfolio project for the [Code Institute](https://codeinstitute.net/ie/) Full Stack Software Development course. The main goal of this project is to create a full-stack website using Django and PostgreSQL. The website is a shop where users can browse and purchase bicycle or sport related accessories. The website is fully responsive and has a clean and modern design. The website is deployed on Heroku and static and media files are stored on Amazon AWS S3.


The live website can be found [here.](https://velotronix-2a1fbfe0d0b1.herokuapp.com/ "Velotronix")

Admin panel can be found [here.](https://velotronix-2a1fbfe0d0b1.herokuapp.com/admin/login/?next=/admin/ "velotronix Admin Panel.")


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
2. As a user, I want to be able to create an account so that I can have my address saved for future purchases.
1. As a user, I want to be able to view the site on any device I choose so that I can shop on the go.
3. As a user, I want to be able to log in and out of my account so that I can access my profile.
4. As a user, I want to be able to reset my password if I forget it so that I can access my account.
5. As a user, I want to be able to find the products I am looking for easily so that I can find what I want quickly.
6. As a user, I want to be able to view the details of a product so that I can decide if I want to purchase it.
7. As a user, I want to be able to add a product to my shopping bag so that I can purchase it.
8. As a user, I want to be able to edit the quantity of a product in my shopping bag so that I can purchase the quantity I want.
9. As a user, I want to be able to delete a product from my shopping bag so that I can remove it if I change my mind.
10. As a user, I want to be able to view my shopping bag so that I can see the total cost of my purchase.
11. As a user, I want to be able to checkout securely so that I can safely purchase my items.
12. As a user, I want to be able to view my order history so that I can see what I have purchased in the past.
12. As a user, I want to be able to add or edit my billing and shipping information so that I can easily checkout.
13. As a user, I want to be able to leave a review for a product so that I can share my experience with other users.
14. As a user, I want to be able to view other users reviews so that I can decide if I want to purchase the product.
15. As a user, I want to be able to edit my reviews so that I can update them if I change my mind.
16. As a user, I want to be able to delete my reviews so that I can remove them if I change my mind.
17. As a user, I want to be able to search for a product by name or description so that I can find what I want quickly.
18. As a user, I want to be able to add a product to the favorites list so that I can purchase it later.
19. As a user, I want to be able to view my favorites list so that I can see what I have saved.
20. As a user, I want to be able to remove a product from my favorites list so that I can remove it if I change my mind.


# Design

### Look and feel


### Colour


### Typography


### Wireframes

#### Home Page desktop Wireframe

![Home Page Wireframe](/static/images/readme_images/wireframes/home_desktop.png)

<details>
<summary>Home Page mobile Wireframe</summary>

![Home Page Wireframe](/static/images/readme_images/wireframes/home_mobile.png)
</details>

<details>
  <summary>Products Page Desktop Wireframe</summary>

![Products Page Wireframe](/static/images/readme_images/wireframes/producs_desktop.png)

</details>
<details>
  <summary>Products Page Mobile Wireframe</summary>
  
![Products Page Wireframe](/static/images/readme_images/wireframes/producs_mobile.png)

</details>

</details>
<details>
  <summary>Product Details Page Desktop Wireframe</summary>
  
![Products Page Wireframe](/static/images/readme_images/wireframes/product_details_desktop.png)

</details>

</details>
<details>
  <summary>Product Details Page Mobile Wireframe</summary>
  
![Products Page Wireframe](/static/images/readme_images/wireframes/product_details_mobile.png)

</details>

# Database Schemas

![Database Schema](/static/images/readme_images/wireframes/erds.png)

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
- [Django](https://www.djangoproject.com/) was used as the main framework for the project.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) was used to style Django forms.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) was used to handle user authentication.
- [Django Mathfilters](https://pypi.org/project/django-mathfilters/) was used to perform calculations in templates.
- [Django Storages](https://django-storages.readthedocs.io/en/latest/) was used to store static and media files on Amazon AWS S3.



### Other tools and programs.
- [Amazon AWS S3](https://aws.amazon.com/) was used to store static and media files.
- [Amazon AWS IAM](https://aws.amazon.com/iam/) was used to create a user for the project.
- [Amazon RDS](https://aws.amazon.com/rds/) was used to create a PostgreSQL database.
- [Font Awesome](https://fontawesome.com/) was used for all icons.
- [Balsamiq](https://balsamiq.com/) was used to create the wireframes.
- [Coolors](https://coolors.co/) was used to create the colour palette.
- [Favicon.io](https://favicon.io/) was used to create the favicon.
- [Birme](https://www.birme.net) was used to convert static images to .webp format.
- [ami.responsivedesign.is](http://ami.responsivedesign.is/) was used to create the mockup image.
- [Lucid](https://lucid.co/) was used when creating database ERD.
- [Visual Studio Code.](https://code.visualstudio.com/) Did all of my coding and synchronizing with GitHub on VS Code.
- [Git](https://git-scm.com/) for version control.
- [GitHub](https://github.com/) for hosting repositories.
- [Heroku](https://www.heroku.com/) where the website is deployed.
- [Grammarly](https://www.grammarly.com/) was used to double-check spelling mistakes.


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


## SEO and Web Marketing.

### Facebook Business Page

### Email Marketing

### Keywords

### Robots.txt

### Sitemap.xml

# Testing
All Testing documentation can be found [here.](./TESTING.md)


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
- Hero image on the home by Photo by [Marianna Lutkova](https://unsplash.com/@mery_lu_design?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/a-person-riding-a-bike-in-a-field-at-sunset-4PSLAKVQQ88?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).

- JavaScript code for the details page image popup was taken from [CodeHim](https://www.codehim.com/lightbox/onclick-image-popup-jquery-lightbox/) and modified to suit my needs. Author of the code is AleMay96.
  


# Credits
