Go back to [README.md](/README.md)

# Testing

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

#### Techmeme project app

| File | Result |
| --- | --- |
| settings.py | ![PEP8 Linter](/static/images/readme_images/pep8_clear.png) |
| urls.py | All clear, no errors found |



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