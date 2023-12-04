Go back to [README.md](/README.md)

# Testing

# Table of contents

- [Testing](#testing)
  - [Code Validation](#code-validation)
    - [Google lighthouse Validation](#google-lighthouse-validation)
    - [CSS Validation](#css-validation)
    - [HTML Validation](#html-validation)
    - [JavaScript Validation](#javascript-validation)
    - [PEP8 Code Institute Python Linter Validation](#pep8-code-institute-python-linter-validation)
      - [Velotronix project app](#velotronix-project-app)
      - [Profiles app](#profiles-app)
      - [Products app](#products-app)
      - [Payment app](#payment-app)
      - [Home app](#home-app)
      - [Cart app](#cart-app)
      - [About app](#about-app)
- [Manual Testing](#manual-testing)
    - [Devices and browsers used for testing](#devices-and-browsers-used-for-testing)
    - [User Stories Testing](#user-stories-testing)
    - [Home Page Testing.](#home-page-testing)
    - [All Products Page Testing.](#all-products-page-testing)
    - [About Page Testing.](#about-page-testing)
    - [Product Details Page Testing.](#product-details-page-testing)
    - [Product Management Page Testing.](#product-management-page-testing)
    - [User Profile Page Testing.](#user-profile-page-testing)
    - [Shopping Cart Page Testing.](#shopping-cart-page-testing)
    - [Checkout Page Testing.](#checkout-page-testing)
    - [Logout Page Testing.](#logout-page-testing)
    - [Login Page Testing.](#login-page-testing)
    - [Password Reset Page Testing.](#password-reset-page-testing)
    - [Sign Up Page Testing.](#sign-up-page-testing)

## Code Validation

### Google lighthouse Validation

All pages were tested with [Google Chrome Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/). Testing was performed in private browsing mode and on the live website on Heroku.

| Page | Image |
| --- | --- |
| Home | ![Home](/static/images/readme_images/lighthouse/index.png) |
| All Products | ![All Products](/static/images/readme_images/lighthouse/all_products.png) |
| Product Details | ![Product Details](/static/images/readme_images/lighthouse/product_detail.png) |
| About | ![About](/static/images/readme_images/lighthouse/about.png) |
| Add Product | ![Add Product](/static/images/readme_images/lighthouse/add_product.png) |
| Edit Product | ![Edit Product](/static/images/readme_images/lighthouse/edit_products.png) |
| Cart Empty | ![Cart Empty](/static/images/readme_images/lighthouse/cart_empty.png) |
| Cart with Products | ![Cart with Products](/static/images/readme_images/lighthouse/cart_with_product.png) |
| Checkout | ![Checkout](/static/images/readme_images/lighthouse/checkout.png) |
| Checkout Success | ![Checkout Success](/static/images/readme_images/lighthouse/checkout_success.png) |
| Profile | ![Profile](/static/images/readme_images/lighthouse/profile.png) |
| Login | ![Login](/static/images/readme_images/lighthouse/login.png) |
| logout | ![Logout](/static/images/readme_images/lighthouse/logout.png) |
| Sign Up | ![Sign Up](/static/images/readme_images/lighthouse/signup.png) |
| Password Reset | ![Password Reset](/static/images/readme_images/lighthouse/forgot_password.png) |

### CSS Validation
- No errors were found when passing through the official [W3C](https://validator.w3.org/) validator.
![CSS Validator](/static/images/readme_images/validators/css_validator.png)

### HTML Validation

- All pages were passed through the official [W3C](https://validator.w3.org/nu/) validator.
- Validating was done by a live website on Heroku. Some errors were found but they were fixed immediately.

| Page | Image |
| --- | --- |
| Home | ![Home](/static/images/readme_images/validators/no_error.png) |
| All Products | ![All Products](/static/images/readme_images/validators/no_error.png) |
| Product Details | ![Product Details](/static/images/readme_images/validators/product_detail.png) |
| | Product Details returned 60 CSS parse errors. All coming from Django_Summernote. Product detail page has description and specification fields that are using Django_Summernote. |

<details>
    <summary>Add Product and edit product</summary>

- Add Product returned 16 different errors. All coming from Django_Summernote. Add Product page has description and specification fields that are using Django_Summernote.
- Given more time I would like to try to fix these errors.
- Because these pages are using same form they have same errors. 

![Add Product](/static/images/readme_images/validators/add_product1.png)
![Add Product](/static/images/readme_images/validators/add_product2.png)
![Add Product](/static/images/readme_images/validators/add_product3.png)
![Product Management](/static/images/readme_images/validators/no_error.png)

- About page returned 4 errors. All coming from Django_Summernote.

![About](/static/images/readme_images/validators/about.png)

</details>

<details>
    <summary>Edit About</summary>

- Edit About page returned 36 errors. All coming from Django_Summernote.

    ![Edit Product](/static/images/readme_images/validators/edit_about1.png)
    ![Edit Product](/static/images/readme_images/validators/edit_about2.png)
    ![Edit Product](/static/images/readme_images/validators/edit_about3.png)
    ![Edit Product](/static/images/readme_images/validators/edit_about4.png)
    ![Edit Product](/static/images/readme_images/validators/edit_about5.png)
    ![Edit Product](/static/images/readme_images/validators/edit_about6.png)

</details>

| Page | Image |
| --- | --- |
| Cart Empty | ![Cart Empty](/static/images/readme_images/validators/no_error.png) |
| Cart with Products | ![Cart with Products](/static/images/readme_images/validators/no_error.png) |
| Profile | ![Profile](/static/images/readme_images/validators/profile.png |
|         | Profile returned 1 error. Missing alt tag on image. That image is a flag in django-countries. |
| Checkout | ![Checkout](/static/images/readme_images/validators/no_error.png) |
| Checkout Success | ![Checkout Success](/static/images/readme_images/validators/no_error.png) |
| Login | ![Login](/static/images/readme_images/validators/no_error.png) |
| logout | ![Logout](/static/images/readme_images/validators/no_error.png) |
| Sign Up | ![Sign Up](/static/images/readme_images/validators/no_error.png) |
| Password Reset | ![Password Reset](/static/images/readme_images/validators/no_error.png) |


### JavaScript Validation

- All JavaScript files were passed through the official [JSHint](https://jshint.com/) validator.

| File | Image |
| --- | --- |
| main.js | ![main.js](/static/images/readme_images/validators/js.png) |


### PEP8 Code Institute Python Linter Validation

- All Python files were passed through the Code Institute [PEP8](https://pep8ci.herokuapp.com/) validator.

#### Velotronix project app

| File | Result |
| --- | --- |
| settings.py | ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)
| urls.py |  ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)
| views.py |  ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)



#### Profiles app

| File | Result |
| --- | --- |
| admin.py | ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)
| apps.py |  ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)
| forms.py |  ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)
| models.py |  ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)
| urls.py |  ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)
| views.py |  ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)

#### Products app

| File | Result |
| --- | --- |
| admin.py | ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)
| apps.py |  ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)
| forms.py |  ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)
| models.py |  ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)
| urls.py |  ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)
| views.py |  ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)

#### Payment app

| File | Result |
| --- | --- |
| admin.py | ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)
| apps.py |  ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)
| forms.py |  ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)
| models.py |  ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)
| urls.py |  ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)
| signals.py |  ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)
| views.py |  ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)
| webhooks.py |  ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)
| webhook_handler.py |  ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)

#### Home app

| File | Result |
| --- | --- |
| urls.py |  ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)
| views.py |  ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)

#### Cart app

| File | Result |
| --- | --- |
| context.py |  ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)
| urls.py |  ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)
| views.py |  ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)

#### About app

| File | Result |
| --- | --- |
| admin.py | ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)
| apps.py |  ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)
| forms.py |  ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)
| models.py |  ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)
| urls.py |  ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)
| views.py |  ![PEP8 Linter]( /static/images/readme_images/validators/ci_linter_clear.png)


# Manual Testing

### Devices and browsers used for testing

This e-commerce website was tested on multiple devices and browsers. All tests were performed in private browsing mode.
| Device | Browser | Result |
| --- | --- | --- |
| Dell Windows 10 desktop computer | Google Chrome | Works as expected |
| Dell Windows 10 desktop computer | Microsoft Edge | Works as expected |
| Dell Windows 10 desktop computer | Mozilla Firefox | Works as expected |
| Dell Windows 10 desktop computer | Opera | Works as expected |
|HP Windows 11 laptop 13" Screen | Google Chrome | Works as expected |
|HP Windows 11 laptop 13" Screen | Microsoft Edge | Works as expected |
|HP Windows 11 laptop 13" Screen | Mozilla Firefox | Works as expected |
| Apple iPhone 12 | Safari | Works as expected |
| Apple iPhone 12 | Google Chrome | Works as expected |
| Apple iPhone 12 | Mozilla Firefox | Works as expected |
| Apple iPhone 13 | Safari | Works as expected |
| Apple iPad 10th generation | Safari | Works as expected |

### User Stories Testing

| Expectation | Solution | Image |
| --- | --- | --- |
| As a user I want to be able to create an account | The user can create an account by clicking on the sign up button in the navigation bar. | ![Sign Up](/static/images/readme_images/user_story_testing/signup.png) |
| As a user, I want to be able to view the site on any device I choose so that I can shop on the go. | The website is fully responsive and works on all devices. | ![Responsive](/static/images/readme_images/user_story_testing/responsive.png) |
| As a user, I want to be able to log in and out of my account so that I can access my profile. | The user can log in and out of their account by clicking on the login/logout button in the navigation bar. | ![Login](/static/images/readme_images/user_story_testing/signup.png) |
| As a user, I want to be able to reset my password if I forget it so that I can access my account. | The user can reset their password by clicking on the forgot password button on the login page. | ![Forgot Password](/static/images/readme_images/user_story_testing/forgot_password.png) |
| As a user, I want to be able to find the products I am looking for easily so that I can find what I want quickly. | The user can find the products they are looking for by using the search bar in the navigation bar. | ![Search](/static/images/readme_images/existing_features/top_nav.png) |
| As a user, I want to be able to view the details of a product so that I can decide if I want to purchase it. | The user can view the details of a product by clicking on the product image or the product name. | ![Product Details](/static/images/readme_images/existing_features/product_detail.png) |
| As a user, I want to be able to add a product to my shopping bag so that I can purchase it. | The user can add a product to their shopping cart by clicking on the add to cart button on the product details page. | ![Add to cart](/static/images/readme_images/user_story_testing/add_to_cart.png) |
| As a user, I want to be able to edit the quantity of a product in my shopping bag so that I can purchase the quantity I want. | The user can edit the quantity of a product in their shopping cart by clicking on the quantity field and changing the number. | ![Edit Quantity](/static/images/readme_images/user_story_testing/edit_quantity.png) |
| As a user, I want to be able to delete a product from my shopping bag so that I can remove it if I change my mind. | The user can delete a product from their shopping cart by clicking on the remove button. | ![Remove](/static/images/readme_images/user_story_testing/edit_quantity.png) |
| As a user, I want to be able to view my shopping bag so that I can see the total cost of my purchase. | The user can view their shopping cart by clicking on the shopping cart icon in the navigation bar. | ![Shopping Cart](/static/images/readme_images/existing_features/cart.png) |
| As a user, I want to be able to checkout securely so that I can safely purchase my items. | The user can checkout securely by clicking on the checkout button in the shopping cart. | ![Checkout](/static/images/readme_images/user_story_testing/checkout.png) |
| As a user, I want to be able to view my order history so that I can see what I have purchased in the past. | The user can view their order history by clicking on the profile button in the navigation bar. | ![Profile](/static/images/readme_images/user_story_testing/history.png) |
| As a user, I want to be able to add or edit my billing and shipping information so that I can easily checkout. | The user can add or edit their billing and shipping information by clicking on the profile button in the navigation bar. | ![Profile](/static/images/readme_images/user_story_testing/billing_info.png) |
| As a user, I want to be able to search for a product by name or description so that I can find what I want quickly. | The user can search for a product by name or description by using the search bar in the navigation bar. | ![Search](/static/images/readme_images/existing_features/top_nav.png) |
| As a user, I want to be able to add a product to the favorites list so that I can purchase it later. | The user can add a product to their favorites list by clicking on the heart icon on the product details page. | ![Add to favorites](/static/images/readme_images/user_story_testing/add_to_favorites.png) |
| s a user, I want to be able to view my favorites list so that I can see what I have saved. | The user can view their favorites list by clicking on the profile button in the navigation bar. | ![Profile](/static/images/readme_images/user_story_testing/favorites.png) |
| As a user, I want to be able to remove a product from my favorites list so that I can remove it if I change my mind. | The user can remove a product from their favorites list by clicking on the heart icon. | ![Remove](/static/images/readme_images/user_story_testing/favorites.png) |




### Home Page Testing.

| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
| Click on the logo in the navigation bar | The user is redirected to the home page. | Works as expected. | |
| Enter a search term in the search bar | The user is redirected to the search results page. | Works as expected. | |
! User clicks on the login button in the navigation bar | The user is redirected to the login page. | Works as expected. | |
| User clicks on the sign up button in the navigation bar | The user is redirected to the sign up page. | Works as expected. | |
| User clicks on the shopping cart icon in the navigation bar | The user is redirected to the shopping cart page. | Works as expected. | |
| User clicks on the profile icon in the navigation bar | The user is redirected to the profile page. | Works as expected. | |
| User clicks on the logout button in the navigation bar | The user is logged out and redirected to the home page. | Works as expected. | |
| User selects dropdown navigation menu item in the navigation bar | Dropdown menu opens with relevant links. | Works as expected. | |
| User clicks on any of the navigation links in the dropdown menu | The user is redirected to the relevant page. | Works as expected. | |
| User clicks on the "About Us" link | The user is redirected to the about page. | Works as expected. | |
| User clicks on shop email address on the footer | The user's email client opens with the shop email address in the "To" field. | Works as expected. | |
| User clicks on the Facebook icon on the footer | The user is redirected to the business Facebook page. | Works as expected. | | 
| User clicks on the privacy policy link on the footer | The user is redirected to the privacy policy page. (about page) | Works as expected. | |
| User enters their email address in the newsletter sign up form | If not on list already the user is added to the mailing list and a success message is displayed. | Works as expected. | |

### All Products Page Testing.

- All pages are the same with only sorting and filtering options changing.
- The Navigation bar and footer are the same as on the home page.

| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
| User hovers the cursor over the product card | The product card gets overlay with a semi-transparent layer and "Click for more" button appears. | Works as expected. | |
| User clicks on the product card | The user is redirected to the product details page. | Works as expected. | |
| On the top of the page user can see the number of products found | The number of products found is displayed and it links back to all products page. | Works as expected. | |
| User clicks on the "Arrow down" icon in the sorting dropdown menu | The sorting options are displayed. | Works as expected. | |

### About Page Testing.

- The Navigation bar and footer are the same as on the home page.

| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
| If user is authenticated and admin | The user can see the edit button that redirects to the edit about page. | Works as expected. | |
| When user fills the contact form and clicks on the submit button | Success message is displayed, page is reloaded and form is cleared. | Works as expected. | |
| When user fills out the faq form and clicks on the submit button | Success message is displayed, page is reloaded and form is cleared. | Works as expected. | |

### Product Details Page Testing.

- The Navigation bar and footer are the same as on the home page.

| Action | Expected Result | Actual Result | Image |
| --- | --- | --- | --- |
| User clicks on the product image | The image is displayed in a new window. | Works as expected. | |
| clicks on the quantity field + or - buttons | The quantity is increased or decreased by 1. | Works as expected. | |
| User clicks on the "Add to cart" button | The product is added to the shopping cart and a success message is displayed. | Works as expected. | |
| User clicks on the "Add to favorites" button | The product is added to the favorites list and a success message is displayed. | Works as expected. | |
| User clicks on the "remove from favorites" button | The product is removed from the favorites list and a success message is displayed. | Works as expected. | |
| User clicks on the "keep shopping" button | The user is redirected to the all products page. | Works as expected. | |

### Product Management Page Testing.

- The Navigation bar and footer are the same as on the home page.

| Action | Expected Result | Actual Result |
| --- | --- | --- |
| User clicks on the "Add Product" navigation link | The user is redirected to the add product page. | Works as expected. |
| User clicks on the edit/delete products link | The user is redirected to the edit/delete products page. | Works as expected. |
| on "Add Product" page user clicks on the "Cancel" button | The user is redirected to the product management page. | Works as expected. |
| on "Add Product" page user clicks on the "Add Product" button | The product is added to the database and the user is redirected to the product management page and a success message is displayed. | Works as expected. |
| on "Edit/Delete Products" page user clicks on the "Edit" button | The user is redirected to the edit product page. | Works as expected. |
| on "Edit/Delete Products" page user clicks on the "Delete" button | The product is deleted or hidden from the database and the user is redirected to the product management page and a success message is displayed. | Works as expected. |
| on the bottom of "edit/delete products" page when product deleted if user clicks on un-hide button| Product is made visible again and success message is displayed. | Works as expected. |

### User Profile Page Testing.
    
    - The Navigation bar and footer are the same as on the home page.
    - Page only available to authenticated users.

| Action | Expected Result | Actual Result |
| --- | --- | --- |
| User fills out the billing information and click on the "Update Information" button | The billing information is updated and a success message is displayed. | Works as expected. |
| If there is favorites, a favorites table is displayed, User clicks on the "remove from favorites" button | The product is removed from the favorites list and a success message is displayed. | Works as expected. |
| user clicks on the "add to cart" button | The product is added to the shopping cart and a success message is displayed. | Works as expected. |
| User clicks on the order number | The user is redirected to the product details page. | Works as expected. |


### Shopping Cart Page Testing.

- The Navigation bar and footer are the same as on the home page.

| Action | Expected Result | Actual Result |
| --- | --- | --- |
| User clicks on the shopping cart icon in the top navigation bar | The user is redirected to the shopping cart page. | Works as expected. |
| when no products in the shopping cart user is show empty shopping cart page | The user is shown empty shopping cart page. | Works as expected. |
| When items in the shopping cart user is shown shopping cart page with products | The user is shown shopping cart page with products. | Works as expected. |
| User clicks on the "keep shopping" button | The user is redirected to the all products page. | Works as expected. |
| User clicks on the "checkout" button | The user is redirected to the checkout page. | Works as expected. |
| User clicks on the "remove" button | The product is removed from the shopping cart and a success message is displayed. | Works as expected. |
| User clicks on the "update" button | The product quantity is updated and a success message is displayed. | Works as expected. |
| user clicks on the + or - buttons in the quantity field | The product quantity is updated and a success message is displayed. | Works as expected. |

### Checkout Page Testing.

- The Navigation bar and footer are the same as on the home page.

| Action | Expected Result | Actual Result |
| --- | --- | --- |
| User clicks on the "adjust cart" button | The user is redirected to the shopping cart page. | Works as expected. |
| User clicks on the "complete order" button | The user is redirected to the checkout success page and a success message is displayed. | Works as expected. |

### Logout Page Testing.

- The Navigation bar and footer are the same as on the home page.

| Action | Expected Result | Actual Result |
| --- | --- | --- |
| User clicks on the "logout" button | The user is logged out and redirected to the home page. | Works as expected. |
| User clicks on the "back" button | The user is redirected to the previous page. | Works as expected. |

### Login Page Testing.

- The Navigation bar and footer are the same as on the home page.

| Action | Expected Result | Actual Result |
| --- | --- | --- |
| User clicks on the "login" button | The user is logged in and redirected back to the page they were on. | Works as expected. |
| User clicks on the "forgot password" link | The user is redirected to the password reset page. | Works as expected. |
| User clicks on the "sign up" link within the login form | The user is redirected to the sign up page. | Works as expected. |

### Password Reset Page Testing.

- The Navigation bar and footer are the same as on the home page.

| Action | Expected Result | Actual Result |
| --- | --- | --- |
| User enters their email address and clicks on the "reset password" button | The user is sent an email with a link to reset their password. | Works as expected. |

### Sign Up Page Testing.

- The Navigation bar and footer are the same as on the home page.

| Action | Expected Result | Actual Result |
| --- | --- | --- |
| User enters valid information and clicks on the "sign up" button | Email confirmation is sent to the user and the user is redirected to the login page. | Works as expected. |
| User enters invalid information and clicks on the "sign up" button | The user is redirected to the sign up page and an error message is displayed. | Works as expected. |
| User clicks on the "login" link within the sign up form | The user is redirected to the login page. | Works as expected. |

[Back to top ⇧](#table-of-contents)

Go back to [README.md](/README.md)