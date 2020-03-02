# Jimbo's Guitar Store

A FullStack Django Framework Project for Code Institute.

My project is an E-commerce web application that list and sells vintage electric guitars and other guitar related products targetting collectors and also the casual musician looking for some cool gear to add to their arsenal.

Jimbo Guitars also provide private viewing in-store for some of our very special vintage products that we have acquired over the years. Do call us for any enquiries or to arrange for an appointment to test out some of our vintage electric guitars and gears.

This project is deployed on [heroku](http://jimboguitars.herokuapp.com/)

This project's repository is also available on [github](https://github.com/papadum-is-nice/TGC_Milestone_Project_4)

## Wireframes
Wireframes for this project could be found [here](https://github.com/papadum-is-nice/TGC_Milestone_Project_4/tree/master/static/images/wireframes)

## UX

This web application is specifically designed for members and the public to view and purchase vintage guitar and gear. Users are greeted by our company logo (at top left) and our vision and mission statement on the home page. As for the rare vintage guitars that we have featured below the welcome statement, our customers are required to contact Jimbo's Guitars directly to arrange for an appointment for viewing if they are interested in playing these special pieces we have. Therefore, these items cannot be purchased online via the site. 

We also have a section whereby members can list their preloved gear for sale. Only logged in users are able to list guitar or guitar related gear for sale using the 'sell' link made available in the navbar. 

The search box is made available in the navbar for users to look up any gear they desire. They can use keywords to return products we have available in our inventory. 

The other links on the navbar are for the users to shop, find out more about Jimbo Guitars or to checkout the products added to the shopping cart. Additionally, there is a user account dropdown menu which allows them to sign up and log in or out.

Users who wish to view all the guitars and gear can do so under the "Shop" link located in the Navbar. This will bring them to a new page where all of the items we have in our inventory are displayed with information on price, model, description and star rating neatly laid out. The user can also add items directly to the cart immediately with a simple click of a button. Adding to cart is made available for logged in and members of the public. However, only the logged in users are able to check out and proceed to payment. Members of the public are required to sign up for an account should they want to checkout. There is also a section on the left that allows users to shop by brand for ease of navigation.


Under the shopping cart, users can change quantity or remove the item from the cart as they please. The user can then proceed to the payment page after filling up a form with shipping and payment details. The total amount is displayed clearly for user verification prior to making payment.

For new users who wants to sign up for an account, there is a signup function under the users drop down menu. Existing users who can't remember their passwords or wishes to change their password is able to do so under the forget password link under the login drop down menu.

At each step, flash messages will be displayed on top of the page to inform the user of the steps he/she has taken and whether it is successful or not.

## Features
### Existing Features
- Feature 1 - Navbar allows users to navigate to other parts of the website with a simple click. The 'Jimbo Guitars' text is a also a link that brings the user back to the home page no matter where the user is at currently on the website

- Feature 2 - Users are able to search for guitar models, name, brand, music gear or any other keywords using the search box

- Feature 3 - Users are able to view all the products listed in the Shop. Each product has its brand, model, color, price and description of the product displayed neatly. The user can also add the product to the cart by clicking the Add to Cart button

- Feature 4 - Under the shopping cart page, users can view the products they choose, make changes to the quantity and click on the apply button to confirm or to remove the product from the cart. The total price is listed clearly and users will then proceed to the next payment stage by clicking the place order button

- Feature 5 - Users are checked if they are signed in before being allowed to make payment. User is taken to a page to fill up shipping info after they log in after which they will be taken to the payment page.

- Feature 6 - New users are able to register for a new user account by creating a username and password

- Feature 7 - Users with an existing account are able to login and  view their own profile page under the user dropdown menu available on the navbar

- Feature 8 - Users can reset their password by entering their registered email address in the password reset page

- Feature 9 - Users are able to login and logout anytime 

### Features Left to Implement
Feature ideas would be :
- to fill up user personal particulars at the checkout page if a user is already logged in 

- to include more than one hi res photo of the guitar on sale


## Technologies Used
- Python : The programming language used for this backend project

- Django : The Python framework used to route urls and for the database

- Jinja2 : The Python Template Engine used to display data from gathered by python onto html

- Bootstrap (getbootstrap.com) : Bootstrap is used to enable mobile responsive webpages

- Heroku (https://www.heroku.com) : 
Heroku is used as a platform to host this project

- Stripe : Stripe is used to test payment

## Testing
I did manual testing as follows :
1. Home:
    1. Go to the url "http://jimboguitars.herokuapp.com/"
    2. Checked that correct html loaded with navabar with logo seen, welcome text is visible and display of feature products

2. Shop:
    1. Click on the "Shop" link on nav bar and verified that the page loads the correct page displaying all the guitars and gear
    2. Navbar is visible
    3. Clicking the add to cart button would add the product to the cart. Also, a flash message would be displayed to show 'new item has been added to your cart!' for the 1st time the product is added and 'Item is already in your shopping cart' if the item is added again

3. Shopping Cart:   
    1. Verified that each product has a number input field and increment / decrement arrow to press to increase or decrease item.
    2. Verified that clicking Apply button the quantity would display the correct number
    3. Clicking on the Remove from Cart button would remove the item from the shopping cart
    4. The Total Price displays the correct amount with the correct quantity * price
    5. Clicking on the place order button would bring me to a page where there is a form to fill name, address and other information 

4. Checkout:
    1. Non-login users would be invited to login when visiting this page
    2. If a user is logged in and after filling in the form, upon clicking on the checkout button would bring the user to the Stripe payment page

5. Signup:
    1. Click on "Signup" at navbar and verified that correct html loaded with form to be inputted and navbar and search bar is visible
    2. Check username, password and password confirmation fields are required and verified that the user cannot continue unless all these are keyed in
    3. Typing in invalid characters each field to see the error messages appear
    4. Typing in correct and valid inputs and click on "Sign up" button would have the user signed in status by the display of the username on the navbar

5. Profile:
    1. While still logged in, click on "Profile" and verified that correct html page loads and navbar and search bar is visible
    2. Verified that username shown is the same as the one on the navbar

6. Log Out:
    1. Clicking on "Logout" button on the navbar would log the user out and display a 'Thank you, see you again!' image
    2. Verified that message on top says "Logged out!"
    3. Verified that number beside Cart at navbar has disappeared
    4. The shopping cart shows that it is now empty and the total price is $0
    
7. Login:
    1. Click on "Login" at navbar and verified that correct html page loads and navbar and search bar is visible
    2. Leave username and password fields empty to see error messages
    3. Fill in wrong characters to see error messages
    4. Fill in correct characters to  verify that user could log in

8. Password Reset:
    1. User is brought to this page with clicking on the forget password link on the login page
    2. Typing in invalid email and verified that field must be filled correctly
    3. Typing in valid email address, and verified that message appears "Success! ...."

9. Edit:
    1. While logged In, the user is brought to the edit form of the product with a click on the edit button of a product in the shop.
    2. The form is prefilled with information from the database
    3. Clicking on the update button would overwrite the current information in the database

9. Different Browsers:
    1. Each web page looks equally good in desktop Chrome, Firefox, Internet Explorer, Opera, Edge
    2. The website is responsive and looks good in mobile browser view

## Deployment
- I followed our instructor, Paul Chor's deployment document

DEPLOYING DJANGO ON HEROKU

Install the following using pip3:
````
sudo pip3 install gunicorn
sudo pip3 install psycopg2
sudo pip3 install whitenoise
````
Add Whitenoise to the middleware inside settings.py
````
MIDDLEWARE = [
.....
'whitenoise.middleware.WhiteNoiseMiddleware',
]
````
Add these for static files:
````
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
````
CREATE these folders at the project level
"Static, media, staticfiles"

Create a static folder in the workspace (where manage.py is) and place an image file inside for testing

Create a staticfiles folder in the workspace and create an empty text file inside there for testing

Create a requirements.txt file using bash in the terminal
`pip3 freeze --local > requirements.txt`

Create a local git repo for your project and connect it to a GitHub repo. Include the relevant .gitignore file. 
````
sudo git init 
sudo git add .
sudo git commit -m "First commit"
sudo git remote add origin <GITHUB REMOTE URL> https://github.com/papadum-is-nice/TGC_Milestone_Project_4
sudo git push origin master
````

Create a .gitignore file and type in `.c9` and add all from [here](https://raw.githubusercontent.com/jpadilla/django-project-template/master/.gitignore)

Log into heroku by typing in `heroku login` and pressing ENTER

Create an app and use a name of your choice
````
heroku create <PROJECT NAME> jimboguitars
git remote -v
````
ADDING POSTGRES SQL

Type in terminal:
`heroku addons:create heroku-postgresql`

Install with pip3:
`sudo pip3 install dj_database_url`

Check the url of the database:
`heroku config`

Go settings.py, comment out the DATABASES section

Add the URL to the database configurations inside settings.py
`import dj_database_url`

````
DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}
````
THEN COPY AND PASTE THE WHOLE postgres link as a STRING
````
DATABASES = {'default': dj_database_url.parse("<long link from heroku website>”)}
````

Put all sensitive data and links  into env.py file and settings.py to link to env.py:
os.environ.setdefault("STRIPE_PUBLISHABLE", "")
os.environ.setdefault("STRIPE_SECRET", "")
os.environ.setdefault("DATABASE_URL", "")

Do migrations and create the superuser
````
python3 manage.py migrate
heroku run python manage.py createsuperuser
````

DEPLOYING
Commit the changed files
````
sudo pip3 freeze --local
sudo git add .
git commit -m "<YOUR COMMENT MESSAGE>"
git push origin master
````

Create the Procfile:
`touch Procfile`

Enter this into the Procfile:
`web: gunicorn <PROJECT_FOLDER>.wsgi:application`
Eg. web: gunicorn jimboguitars_project.wsgi:application (name of the project folder where settings.py, urls.py wsgi.py are)

Add the URL of the heroku app into the ALLOWED_HOST inside settings.py

Add and commit
````
sudo git add .
sudo git push heroku 
````

Go to Heroku, click on the Open App button on top of the page

## Credits
- Paul and John for all their help
- Google and stackoverflow for lots of troubleshooting

### Media
- pictures are all searches via google images for keywords
- photos and description of featured vintage guitars from www.emeraldcityguitars.com
- photos and description of guitars/amp in shop from www.fender.com, www.gibson.com, www.gretchguitars.com, www.taylorguitars.com, www.martinguitar.com

### This for educational use