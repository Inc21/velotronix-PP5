![VeloTronix Logo](/static/images/readme_images/velotronix_logo.png)
![mockup](/static/images/readme_images/mockup.png)

# Introduction
Velotronix is a fictional e-commerce website created for my fifth portfolio project for the [Code Institute](https://codeinstitute.net/ie/) Full Stack Software Development course. The main goal of this project is to create a full-stack website using Django and PostgreSQL. The website is a shop where users can browse and purchase bicycle or sport related accessories. The website is fully responsive and has a clean and modern design. The website is deployed on Heroku and static and media files are stored on Amazon AWS S3.


The live website can be found [here.](https://velotronix-2a1fbfe0d0b1.herokuapp.com/ "Velotronix")

Admin panel can be found [here.](https://velotronix-2a1fbfe0d0b1.herokuapp.com/admin/login/?next=/admin/ "velotronix Admin Panel.")

To complete mock payments you can use the following test card details:
![Card Details](/static/images/readme_images/card.png)


### Project Goals

- To create a full-stack website using Django and PostgreSQL.
- To create a website that is fully responsive and has a clean and modern design.
- To create a website that is easy to navigate and use.
- To create a website that is easy to maintain and update.
- To create a website that is secure and safe to use.
- To create a website that is accessible to all users.
- To create a website that is SEO friendly.
- To create a website that is user friendly.
- To create a e-commerce website that allows users to browse and purchase products.
- To create a e-commerce website that allows users to create an account and save their details for future purchases.


### Project Goals

# Table of contents

- [SEO and Web Marketing.](#seo-and-web-marketing)
    - [Business Model](#business-model)
    - [SEO](#seo)
    - [Web Marketing](#web-marketing)
- [User Stories](#user-stories)
    - [Developer](#developer)
    - [User/shopper](#usershopper)
- [Design](#design)
    - [Look and feel](#look-and-feel)
    - [Colour](#colour)
    - [Typography](#typography)
    - [Wireframes](#wireframes)
      - [Home Page desktop Wireframe](#home-page-desktop-wireframe)
- [Database Schemas](#database-schemas)
    - [auth_user / User model](#auth_user--user-model)
    - [UserProfile model - profiles app](#userprofile-model---profiles-app)
    - [Product model - product app](#product-model---product-app)
    - [Category model - Product app](#category-model---product-app)
    - [Order model - payment app](#order-model---payment-app)
    - [OrderLineItem model - payment app](#orderlineitem-model---payment-app)
    - [About model - about app](#about-model---about-app)
    - [Contact model - about app](#contact-model---about-app)
    - [faq model - about app](#faq-model---about-app)
- [Agile Development](#agile-development)
- [Tools and technologies used](#tools-and-technologies-used)
    - [Languages and Frameworks](#languages-and-frameworks)
    - [Main Django Packages](#main-django-packages)
      - [Other Django Packages](#other-django-packages)
    - [Other tools and programs.](#other-tools-and-programs)
- [Existing Features](#existing-features)
    - [Header](#header)
    - [Contact and FAQ Form emails](#contact-and-faq-form-emails)
    - [Footer](#footer)
    - [Home Page](#home-page)
    - [Products Page](#products-page)
    - [Product Details Page](#product-details-page)
    - [Product Management Page](#product-management-page)
    - [About Page](#about-page)
    - [Shopping Cart Page](#shopping-cart-page)
    - [Checkout Page](#checkout-page)
    - [Profile Page](#profile-page)
    - [Login Page](#login-page)
    - [Logout Page](#logout-page)
    - [Sign-up Page](#sign-up-page)
    - [Password Reset Page](#password-reset-page)
    - [Custom Error 404 Page](#custom-error-404-page)
  - [Features Left to Implement](#features-left-to-implement)
- [Testing](#testing)
  - [Interesting bugs or problems](#interesting-bugs-or-problems)
    - [Bug 1](#bug-1)
  - [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
    - [Deploy with Heroku](#deploy-with-heroku)
    - [Clone project](#clone-project)
    - [Fork repository](#fork-repository)
- [Content](#content)
- [Credits](#credits)



# SEO and Web Marketing.

### Business Model

Velotronix is a business to consumer (B2C) e-commerce website. 
The main goal of the website is to sell bicycle and sport related accessories. The website is aimed at people who are interested in cycling and other sports. The website is designed to be easy to navigate and use. The website is designed to be easy to maintain and update. The website is designed to be secure and safe to use. The website is designed to be accessible to all users. The website is designed to be SEO friendly. The website is designed to be user friendly. The website is designed to allow users to browse and purchase products. The website is designed to allow users to create an account and save their details for future purchases. Velotronix will deliver internationally but main customers will be from Ireland and aiming to deliver within 1-2 business days.

- Provide a safe and secure website for users to browse and purchase products.
- Deliver quality products to customers.
- Provide efficient and reliable delivery service.


### SEO

- Descriptive meta tags were added to base.html which is extended on all the pages. Including title, description and keywords. Meta tags are important for SEO as they help search engines to understand what the page is about. Meta tags are also important for accessibility as they are used by screen readers to describe the page to the user.
- Used [xml-sitemaps](https://www.xml-sitemaps.com/ "xml-sitemaps") to generate sitemap.xml file. Sitemap.xml file is important for SEO as it helps search engines to crawl the website. Sitemap.xml file is also important for accessibility as it helps screen readers to navigate the website.
- Used [robots.txt](https://www.robotstxt.org/ "robots.txt") to tell search engines which pages to crawl and which pages to ignore. robots.txt file is important for SEO as it helps search engines to crawl the website. robots.txt file is also important for accessibility as it helps screen readers to navigate the website.
- Add rel attribute to all links. rel attribute is important for SEO as it helps search engines to understand the relationship between pages. rel attribute is also important for accessibility as it helps screen readers to navigate the website.

### Web Marketing

- Created a [Facebook Business Page](https://www.facebook.com/people/Velotronix/61554100205665/ "Facebook Business Page")
 for the website. Facebook business page is important for web marketing as it helps to reach a wider audience.


![Facebook Business Page](/static/images/readme_images/facebook_page.png)


- Newsletter sign up form was added to the footer of the website. This one field form is designed to be easy to use and fill out. Newsletter sign up form is important for web marketing as it helps to reach a wider audience. Service is provided by [Mailchimp](https://mailchimp.com/ "Mailchimp").


![Newsletter Sign Up Form](/static/images/readme_images/subscribe.png)


Seo and marketing are possibly the most important aspects of any e-commerce website. Without them, the website will not be found by potential customers. Given my time restraints and if it would be a real world project, these areas could be improved upon. I would add more meta relevant meta tags and more do more market research to find out what keywords to use. I would also add more content to the website to improve SEO. I would also add more marketing strategies to reach a wider audience. Including more social media platforms and email marketing.


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


With the design for this e-commerce website was chosen to be clean and modern. Both colours and typography were chosen to be easy on the eye and to create a relaxing atmosphere while being very high in contrast and easy to read. Main colour for the website is nice darker shade of green and off-white being used as a background colour to make website more comfortable to browse.


### Colour

Colour palette was created with [Coolors](https://coolors.co/).

![Color Palette](/static/images/readme_images/colour_palette.png)

### Typography

- [Google Fonts](https://fonts.google.com/) was used for the font. 

Font used for the website is "Sometype Mono". This font was chosen for its clean and modern look. It is also very easy to read and has a high contrast. This font is used for all text on the website. This font is very accessible as it is easy to read and has a high contrast. This font is also very easy to read on all devices and screen sizes. 
Sans-serif is used as a fallback font in case the font fails to load for any reason. Sans-serif is also very easy to read and has a high contrast. Sans-serif is also very easy to read on all devices and screen sizes.

| Font Weight 400 | Font Weight 700 |
| --- | --- |
| ![Sometype Mono 400](/static/images/readme_images/sometype-mono-400.png) | ![Sometype Mono 700](/static/images/readme_images/sometype-mono-700.png) |


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

![Database Schema](/static/images/readme_images/erds.png)

### auth_user / User model

- The user model is the default Django user model.

| key | Field Type | Validation |
| --- | --- | --- |
| id | IntegerField | |
| password | CharField |  |
| last_login | DateTimeField |  |
| is_superuser | BooleanField |  |
| username | CharField | max_length=150, unique=True |
| first_name | CharField | max_length=150, blank=True |
| last_name | CharField | max_length=150, blank=True |
| email | EmailField | max_length=254, unique=True |
| is_staff | BooleanField |  |
| is_active | BooleanField |  |
| date_joined | DateTimeField |  |


### UserProfile model - profiles app

- UserProfile model is connected to the User model with OneToOneField. This model is used to store extra user information.

| key | Field Type | Validation |
| --- | --- | --- |
| user | OneToOneField | User, on_delete=models.CASCADE |
| full_name | CharField | max_length=50, null=True, blank=True |
| email | EmailField | max_length=254, null=True, blank=True |
| phone_number | CharField | max_length=20, null=True, blank=True |
| country | CountryField | blank_label="Country", max_length=40, null=True, blank=True |
| postcode | CharField | max_length=20, null=True, blank=True |
| town_or_city | CharField | max_length=40, null=True, blank=True |
| street_address1 | CharField | max_length=80, null=True, blank=True |
| street_address2 | CharField | max_length=80, null=True, blank=True |
| county | CharField | max_length=80, null=True, blank=True |
| created | DateTimeField | auto_now_add=True |


### Product model - product app

- The Product model is used to store all the product information.

| key | Field Type | Validation |
| --- | --- | --- |
| id | AutoField | primary_key=True |
| category | ForeignKey | 'Category', null=True, blank=True, on_delete=models.SET_NULL |
| sku | CharField | max_length=255, null=True, blank=True |
| name | CharField | max_length=50 |
| brand | CharField |  max_length=255, null=True, blank=True |
| description | TextField |  null=True, blank=True |
| specs | TextField | null=True, blank=True |
| on_sale | BooleanField | default=False |
| price | DecimalField | max_digits=6, decimal_places=2 |
| sale_price | DecimalField | max_digits=6, decimal_places=2 |
| image1 | ResizedImageField | size=[500, 400], upload_to='product_images/', null=True, force_format='WEBP', quality=85, blank=True, default='product_images/noimage.webp' |
| image2 | ResizedImageField | size=[500, 400], upload_to='product_images/', null=True, force_format='WEBP', quality=85, blank=True, default='product_images/noimage.webp' |
| image3 | ResizedImageField | size=[500, 400], upload_to='product_images/', null=True, force_format='WEBP', quality=85, blank=True, default='product_images/noimage.webp' |
| image4 | ResizedImageField | size=[500, 400], upload_to='product_images/', null=True, force_format='WEBP', quality=85, blank=True, default='product_images/noimage.webp' |
| popularity | IntegerField | default=0 |
| favorites | ManyToManyField | User, related_name='favorites', blank=True, default=None |
| added_date | DateTimeField | auto_now_add=True, blank=True, null=True |
| hidden | BooleanField | default=False |


### Category model - Product app

| key | Field Type | Validation |
| --- | --- | --- |
| id | AutoField | primary_key=True |
| name | CharField | max_length=255 |
| friendly_name | CharField | max_length=255, null=True, blank=True |


### Order model - payment app

- The Order model is used to store all the order information.

| key | Field Type | Validation |
| --- | --- | --- |
| order_number | CharField | max_length=32, null=False, editable=False |
| user_profile | ForeignKey | UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders' |
| full_name | CharField | max_length=50, null=True, blank=True |
| email | EmailField | max_length=254, null=True, blank=True |
| phone_number | CharField | max_length=20, null=True, blank=True |
| country | CountryField | blank_label="Country", max_length=40, null=True, blank=True |
| postcode | CharField | max_length=20, null=True, blank=True |
| town_or_city | CharField | max_length=40, null=True, blank=True |
| street_address1 | CharField | max_length=80, null=True, blank=True |
| street_address2 | CharField | max_length=80, null=True, blank=True |
| county | CharField | max_length=80, null=True, blank=True |
| date | DateTimeField | auto_now_add=True |
| delivery_cost | DecimalField | max_digits=6, decimal_places=2, null=False, default=0 |
| order_total | DecimalField | max_digits=6, decimal_places=2, null=False, default=0 |
| grand_total | DecimalField | max_digits=6, decimal_places=2, null=False, default=0 |
| original_bag | TextField | null=False, blank=False, default='' |
| stripe_pid | CharField | max_length=254, null=False, blank=False, default='' |


### OrderLineItem model - payment app

- The OrderLineItem model is used to store all the order line item information.

| key | Field Type | Validation |
| --- | --- | --- |
| order | ForeignKey | Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' |
| product | ForeignKey | Product, null=False, blank=False, on_delete=models.CASCADE |
| quantity | IntegerField | null=False, blank=False, default=0 |
| lineitem_total | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False |


### About model (custom model 1) - about app 

- The About model is used to store all the about us information.

| key | Field Type | Validation |
| --- | --- | --- |
| name | CharField | max_length=254, null=False, blank=False, default="velotronix" |
| delivery_info | TextField | null=True, blank=True |
| returns_info | TextField | null=True, blank=True |
| faq | TextField | null=True, blank=True |
| privacy_policy | TextField | null=True, blank=True |


### Contact model (custom model 2) - about app

- The Contact model is used to create contact form and store all the contact information.

| key | Field Type | Validation |
| --- | --- | --- |
| author | CharField | max_length=254, null=False, blank=False |
| email | EmailField | max_length=254, null=False, blank=False |
| subject | CharField | max_length=254, null=False, blank=False |
| message | TextField | null=False, blank=False |
| created | DateTimeField | auto_now_add=True |
| id | AutoField | primary_key=True |


### faq model (custom model 3) - about app

- The faq model is used to store all the frequently asked questions and create faq form for user to submit their questions.

| key | Field Type | Validation |
| --- | --- | --- |
| faq_name | CharField | max_length=254, null=False, blank=False |
| faq_email | EmailField | max_length=254, null=False, blank=False |
| faq_question | CharField | max_length=254, null=False, blank=False |
| created | DateTimeField | auto_now_add=True |
| id | AutoField | primary_key=True |


# Agile Development

Link to Velotronix [GitHub Agile Project](https://github.com/users/Inc21/projects/7)

This project was my second time using Agile Development. Did find it much more helpful in managing my time than it did previous project. Also added [sprints](https://github.com/Inc21/velotronix-PP5/milestones) using GitHub milestones feature to my agile planning and this increased my time management even further. I decided to use the [Kanban](https://en.wikipedia.org/wiki/Kanban_(development)) and [MoSCoW](https://en.wikipedia.org/wiki/MoSCoW_method) prioritization method again. I used [GitHub Projects](https://github.com/users/Inc21/projects/7) to create the board. 

I created 5 columns: Epics, To-Do, In Progress, Done and Backlog. I also created 9 labels:

- For MoSCoW prioritization: Must Have, Should Have, Could Have, Won't Have.

![Must Have](/static/images/readme_images/labels/must-have.png) ![Should Have](/static/images/readme_images/labels/should-have.png) ![Could Have](/static/images/readme_images/labels/could-have.png) ![Won't Have](/static/images/readme_images/labels/wont-have.png)

- And 5 helper labels: Dev-task, Epic, User-story, In-progress, Done.

![Dev-task](/static/images/readme_images/labels/dev-task.png) ![Epic](/static/images/readme_images/labels/epic.png) ![User-story](/static/images/readme_images/labels/user-story.png) ![In-progress](/static/images/readme_images/labels/in-progress.png) ![Done](/static/images/readme_images/labels/done.png)

-  9 Epics divided into 24 User stories. Epics and user stories are connected with the # link on the title and in the description.
- Project issues were divided into 4 sprints. Sprints were created to according to the available time I had to complete the project. Each sprint was given a 2 week time frame. 
Project then was divided into 10 Epics and 30 User stories and tasks. Epics and user stories are connected with the # link on the title and in the description.

| Example | Image |
| --- | --- |
| Sprint | ![Sprint](/static/images/readme_images/sprints.png) |
| Epic | ![Epic](/static/images/readme_images/epic_example.png) |
| User story | ![User story](/static/images/readme_images/user_storie_example.png) |
| Task | ![Task](/static/images/readme_images/task_example.png) |

- My Kanban board:

| then | now |
| --- | --- |
| ![Kanban board](/static/images/readme_images/kanban.png) | ![Kanban board](/static/images/readme_images/kanban_now.png) |

* Items in the backlog are not being developed at the moment but will be added to the project in the future. They marked with the "Won't Have" label.



# Tools and technologies used

### Languages and Frameworks

This project was created using the following languages and frameworks:

- [Django](https://www.djangoproject.com/) as the Python web framework.
    - [Python](https://www.python.org/) as the backend programming language.
- [HTML](https://en.wikipedia.org/wiki/HTML) as the markup language and templating language.
- [CSS](https://en.wikipedia.org/wiki/CSS) as the style sheet language.
    - [Bootstrap 5](https://getbootstrap.com/) as the CSS framework.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) to create carousel on index.html.
    - [jQuery](https://jquery.com/) to simplify DOM manipulation.

### Main Django Packages
- [Django](https://www.djangoproject.com/) was used as the main framework for the project.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) was used to style Django forms.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) was used to handle user authentication.
- [Django Mathfilters](https://pypi.org/project/django-mathfilters/) was used to perform calculations in templates.
- [Django Countries](https://pypi.org/project/django-countries/) was used to create a country field in the checkout form.
- [Django Resized](https://pypi.org/project/django-resized/) was used to resize images and convert them to .webp format.
- [Django Summernote](https://pypi.org/project/django-summernote/) was used to create a rich text editor for the about us page.
- [Django Storages](https://django-storages.readthedocs.io/en/latest/) was used to store static and media files on Amazon AWS S3.
- [crispy-bootstrap5](https://pypi.org/project/crispy-bootstrap5/) was used to style Django forms with Bootstrap 5.

#### Other Django Packages
[django-bleach](https://pypi.org/project/django-bleach/), [boto3](https://pypi.org/project/boto3/), [dj-database-url](https://pypi.org/project/dj-database-url/),
[gunicorn](https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/gunicorn/), [Pillow](https://pypi.org/project/Pillow/), [psycopg2](https://pypi.org/project/psycopg2/) and others that come with Django and packages above.



### Other tools and programs.
- [Amazon AWS S3](https://aws.amazon.com/) was used to store static and media files.
- [ElephantSQL](https://www.elephantsql.com/) was used to create a PostgreSQL database for development.
- [Amazon AWS IAM](https://aws.amazon.com/iam/) was used to create a user for the project.
- [Font Awesome](https://fontawesome.com/) was used for all icons.
- [Balsamiq](https://balsamiq.com/) was used to create the wireframes.
- [Coolors](https://coolors.co/) was used to create the colour palette.
- [Favicon.io](https://favicon.io/) was used to create the favicon.
- [Birme](https://www.birme.net) was used to convert static images to .webp format. All new content will be automatically converted by Django Resized to .webp format.
- [ami.responsivedesign.is](http://ami.responsivedesign.is/) was used to create the mockup image.
- [Lucid](https://lucid.co/) was used when creating database ERD.
- [Visual Studio Code.](https://code.visualstudio.com/) Did all of my coding and synchronizing with GitHub on VS Code.
- [Git](https://git-scm.com/) for version control.
- [GitHub](https://github.com/) for hosting repositories.
- [Heroku](https://www.heroku.com/) where the website is deployed.
- [Grammarly](https://www.grammarly.com/) was used to double-check spelling mistakes.


# Existing Features

- All pages are responsive on all devices.
- All pages feature a sticky header with the site logo and a navigation bar with links to other pages, login/sign-up links and a search bar. 
- All pages feature a footer with link to privacy policy and social media links.
- All user actions are confirmed with Django messages.
- All user-uploaded content will be automatically converted to .webp format to save space and bandwidth using [Django-resized](https://pypi.org/project/django-resized/).  

![Django messages](/static/images/readme_images/existing_features/messages.png)

**Screenshots and description of existing features are available below in collapsed sections.**

### Header

<details>
  <summary>Header</summary>

  - The header is sticky and available on all pages.
  - On mobile devices the header is collapsed into a hamburger menu including search bar.
  - The header features top navigation bar with search bar, login/sign-up links and a shopping cart icon.

  ![Header](/static/images/readme_images/existing_features/top_nav.png)

  - The header features a logo which is a link to the home page.
  - The lower header features a website logo, navigation bar with links to all products, electronics, accessories and about page. For authenticated users with admin permissions, the navigation bar also includes a link to product management page.

  ![Header](/static/images/readme_images/existing_features/lower_nav.png)

  - Navigation items are in a dropdown menu and will be in a hamburger menu on mobile devices.

  ![Header](/static/images/readme_images/existing_features/nav_all_products.png) ![Header](/static/images/readme_images/existing_features/nav_electronics.png) ![Header](/static/images/readme_images/existing_features/nav_accessories.png) ![Header](/static/images/readme_images/existing_features/nav_about.png) ![Header](/static/images/readme_images/existing_features/nav_admin.png)

</details>

### Contact and FAQ Form emails

<details>
  <summary>Contact and FAQ Form emails</summary>

  - When user submits contact form or FAQ form, email is sent to the site admin and user with the information from the form.

  ![Contact Form](/static/images/readme_images/existing_features/contact_form_email.png) ![FAQ Form](/static/images/readme_images/existing_features/faq_form_email.png)

</details>

### Footer

<details>
  <summary>Footer</summary>

  - The footer is available on all pages.
  - The footer features a link to privacy policy page and social media links.
  - Also features a newsletter sign up form provided by [Mailchimp](https://mailchimp.com/ "Mailchimp").

  ![Footer](/static/images/readme_images/existing_features/footer.png)

</details>

### Home Page

<details>
  <summary>Home page</summary>

  - This page is the first page the user sees when they visit the website.
  - The home page features a hero image with a welcome message and a call to action button to shop now.

  ![Home Page](/static/images/readme_images/existing_features/home_page.png)
</details>

### Products Page

<details>
  <summary>Products page</summary>

  - This page features a list of all products.
  - The products are displayed in a grid with 4 products per row on large screens, 3 products per row on medium screens and 2 products per row on small screens and 1 product per row on extra small screens.
  - Each product displays the product name, price, image and a button to add the product to the shopping cart.

  ![Products Page](/static/images/readme_images/existing_features/all_products.png)

  - When product card is hovered, button "click for more" is rendered. When clicked, user is taken to the product details page.

  ![Products Page](/static/images/readme_images/existing_features/all_products_hover.png)

  - When admin selects "on_sale" checkbox when editing or adding a product, product is displayed with a sale price and a "sale" badge.

  ![Products Page](/static/images/readme_images/existing_features/product_on_sale.png)

  - Free delivery banner is displayed on all product pages.

  ![Products Page](/static/images/readme_images/existing_features/delivery_banner.png)

</details>

### Product Details Page

<details>
  <summary>Product details page</summary>

  - This page features all the information about the product.
  - Each product displays the product name, price, image, description, specs, quantity input and a button to add the product to the shopping cart.
  - If the user is authenticated and they have admin permissions, they will also see a buttons to edit and delete the product.

  ![Product Detail Page](/static/images/readme_images/existing_features/product_detail.png)

  - Also page includes a link to add the product to the favorites list. If user is not authenticated, they will be redirected to the login page. If the product is already in the favorites list, the button text will change to "remove from favorites" and the link will remove the product from the favorites list.

  ![Product Detail Page](/static/images/readme_images/existing_features/product_detail_favorite.png)

</details>

### Product Management Page

<details>
  <summary>Product Management Page</summary>

  - When user is authenticated and they have admin they will see a link to product management page in the navigation bar.

  ![Product Management Page](/static/images/readme_images/existing_features/nav_admin.png)

  Edit Product form:

  - This page features a form to edit the product.
  - The form is pre-populated with the product information.
  - The form includes a button to cancel the edit and return to the product details page.

  ![Edit Product Page](/static/images/readme_images/existing_features/edit_product.png)

  Add Product form:

  - This page features a form to add a new product.
  - The form includes a button to cancel the edit and return to the product details page.

  ![Add Product Page](/static/images/readme_images/existing_features/admin_add_product.png)

  Edit or Delete Product page:

  - Page features all products in a table with a button to edit or delete the product.

  ![Edit or Delete Product Page](/static/images/readme_images/existing_features/edit_delete_products.png)

  - Product soft delete is performed by setting the "hidden" field to True. This way the product is not displayed on the website but is still available in the database. This is done to preserve the order history. If the product is deleted, the order history will be lost. Products can be restored by setting the "hidden" field to False through the edit product form. Products can be permanently deleted through admin panel.

  ![Edit or Delete Product Page](/static/images/readme_images/existing_features/hidden_edit_delete_products.png) 

</details>

### About Page

<details>
  <summary>About page</summary>

  - This page features all the information about the company.
  -  For site admin the about page features a rich text editor to add and edit the about us information inc.
  - If the user is authenticated and they have admin permissions, they will also see a buttons to edit and delete the about us information.

  ![About Page](/static/images/readme_images/existing_features/about_page.png)
  ![About Page](/static/images/readme_images/existing_features/contct_form.png)
  ![About Page](/static/images/readme_images/existing_features/faq_form.png)
  ![About Page](/static/images/readme_images/existing_features/returns.png)
  ![About Page](/static/images/readme_images/existing_features/faq.png)
  ![About Page](/static/images/readme_images/existing_features/delivery_info.png)
  ![About Page](/static/images/readme_images/existing_features/privacy_policy.png)

  Edit About form:

  - For a site admin edit button is displayed on the about page. When clicked, user is taken to the edit about page.

  ![Edit About Page](/static/images/readme_images/existing_features/edit_about.png)

</details>

### Shopping Cart Page 

<details>
  <summary>Shopping Cart Page</summary>

  - Link to the shopping cart page is alway displayed in the top navigation bar. User can see the number of items in the shopping cart and the total cost of the items in the shopping cart. User will navigate to the shopping cart page when they click on the shopping cart icon.
  - When there are items in the shopping cart, user will see a list of all items in the shopping cart. Each item will display the product name, image, price, quantity input, subtotal and a button to remove the item from the shopping cart.

  ![Shopping Cart Page](/static/images/readme_images/existing_features/cart.png)

  - When there is no items in the shopping cart, user will see a message "Your cart is empty".

  ![Shopping Cart Page](/static/images/readme_images/existing_features/empty_cart.png)

</details>

### Checkout Page

<details>
  <summary>Checkout Page</summary>

  - This page features a form to enter billing and shipping information.
  - The form is pre-populated with the user information if the user is authenticated.
  - The form includes a button to cancel the checkout and return to the shopping cart page.
  - The form includes a button to submit the checkout and proceed to the payment page.
  - The customer is shown the order summary including the order total and delivery cost.

  ![Checkout Page](/static/images/readme_images/existing_features/checkout.png)

  - After successful checkout, the customer is redirected to the checkout success page.

  ![Checkout Page](/static/images/readme_images/existing_features/checkout_success.png)

  - Confirmation email is sent to the customer after successful checkout.

  ![Checkout Page](/static/images/readme_images/existing_features/checkout_success_email.png)

</details>

### Profile Page

<details>
  <summary>Profile Page</summary>

  - This page features a form to enter billing and shipping information, favorites list and order history.
  - The form includes a button to cancel the edit and return to the profile page.
  - The form includes a button to submit the edit and update the profile information.
  - The favorites list includes a button to remove the item from the favorites list and a button to add the item to the shopping cart.
  - The customer is shown the order history including the order number, date, items and order total. 

  ![Profile Page](/static/images/readme_images/existing_features/profile_page.png)

  - The customer is shown the order history including the order number, date, items, order total and delivery cost.

</details>

### Login Page

<details>
  <summary>Login Page</summary>

  - Django Allauth was used to handle user authentication.
  - This page features a form to login to the website.
  - The form includes a button to submit the login and login to the website.
  - The customer is shown a link to the sign-up page if they do not have an account.
  - The customer is shown a link to the password reset page if they forgot their password.

  ![Login Page](/static/images/readme_images/existing_features/login.png)

</details>

### Logout Page

<details>
  <summary>Logout Page</summary>

  - Django Allauth was used to handle user authentication.
  - This page features a message to confirm that the user has logged out of the website.

  ![Logout Page](/static/images/readme_images/existing_features/logout_confirm.png)

</details>

### Sign-up Page

<details>
  <summary>Sign-up Page</summary>

  - Django Allauth was used to handle user authentication.
  - This page features a form to sign-up to the website.
  - The form includes a button to submit the sign-up and sign-up to the website.
  - The customer is shown a link to the login page if they already have an account.

  ![Sign-up Page](/static/images/readme_images/existing_features/signup.png)

</details>

### Password Reset Page

<details>
  <summary>Password Reset Page</summary>

  - Django Allauth was used to handle user authentication.
  - This page features a form to reset the password.
  - The form includes a button to submit the password reset and reset the password.

  ![Password Reset Page](/static/images/readme_images/existing_features/password_reset.png)

</details>

### Custom Error 404 Page

<details>
  <summary>Custom Error 404 Page</summary>

  - This page features a message to confirm that the page does not exist.
  - The customer is shown a link to the home page.
  - also custom error 500, 403 and 400 pages were created but not shown here but they are using the same template as the 404 page.

  ![Custom Error 404 Page](/static/images/readme_images/existing_features/404.png)

</details>


## Features Left to Implement

My available time to complete this project was very limited this time around. Many late nights and early mornings were spent on this project. I had to cut some features from the project to be able to complete it on time. I will be adding these features in the future.

- Product quantity in stock. When the product is added to the shopping cart, the quantity in stock will be reduced by the quantity added to the shopping cart. If the quantity in stock is 0, the product will be displayed as out of stock **(Post-course add-on)**
- Pagination on the products page. Currently, all products are displayed on one page. This will cause performance issues when there are many products on the website. Pagination will be added to the products page to display a limited number of products per page. **(Post-course add-on)**
- Product reviews. Customers will be able to leave a review for the product. The review will be displayed on the product details page. **(Post-course add-on)**
- Product rating. Customers will be able to rate the product. The rating will be displayed on the product details page. **(Post-course add-on)**
- A better way of displaying multiple images on the product details page. Currently, the images are displayed as a plain list. I would like to add a carousel or some other js library to display the images. **(Post-course add-on)**
- Social media login. Customers will be able to log in to the website using their social media accounts. Although this feature is not essential, it will make the login process easier for the customer. I have used it in previous projects but just ran out of time to implement it in this project. **(Post-course add-on)**

 

# Testing
All Testing documentation can be found [here.](./TESTING.md)


## Interesting bugs or problems

### Bug 1
 - About midway through development process I had to make a change to the checkout model. At this stage I was still using only SqLite3 database. For some reason, when I tried to migrate the changes to the database, I was getting an error. I tried to fix the error for a few hours but could not find a solution. Even vent into the database and deleted tables manually but still got the same error. I decided to delete the database and start from scratch. I did have to coll it "Payment" instead of "Checkout" but it worked. I did not have any issues with the database after that. I did not have time to investigate this issue further but I will be looking into it in the future. 


## Unfixed Bugs

- Although I did my best to catch all bugs, there are some bugs that I might have missed. 
- Django_Summernote causes many errors while validating HTML. No visible errors or performance issues caused by summernote but its definitely something I will be looking out for before I get this far into the project in the future.

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
    - Open my [GitHub repository](https://github.com/Inc21/velotronix-PP5).
    - Click on the 'Fork' button on the top right of the screen.
    - On the 'Create a new fork' page you are given the option to rename that repository and then click on the green 'Create fork' button at the bottom of the form.


# Content
- Hero image on the home by Photo by [Marianna Lutkova](https://unsplash.com/@mery_lu_design?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/a-person-riding-a-bike-in-a-field-at-sunset-4PSLAKVQQ88?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).

- JavaScript code for the details page image popup was taken from [CodeHim](https://www.codehim.com/lightbox/onclick-image-popup-jquery-lightbox/) and modified to suit my needs. Author of the code is AleMay96.

- [Code Institute](https://codeinstitute.net/ie/) Boutique Ado project was used as a reference for this project.

- All the product images and descriptions were taken from [Wahoofitness.com](https://eu.wahoofitness.com/)

# Credits

It has been another great learning experience. Very tough at times but I am very happy with the result. I have learned a lot and I am looking forward to the next project.
I would like to thank my mentor Dick Vlaanderen for his help and support during this and projects that came before this.

Also would like to thank my family who, even though I abandon them for a year, have stood beside me and supported me all the way.
All my Slack cohort, our facilitator Paul Thomas O’Riordan and a good friend and a super motivator Dayana Nashkova.


[Back to top ⇧](#table-of-contents)
