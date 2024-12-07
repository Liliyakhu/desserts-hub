# Dessert Hub


**DessertHub** is a web application that connects dessert 
enthusiasts by allowing users to share, discover recipes from around the world. 
Whether you're a professional pastry chef or a home baker, 
Dessert Hub provides a platform to explore your passion for sweet creations.
___________
## Features
+ **User Registration and Authentication:** 
Secure user accounts with login and "Remember Me" functionality.
+ **Dessert Sharing:** Users can create, edit, and delete
their own dessert, dessert type and ingredients. 
+ **Search:** Search user by username, dessert, dessert type and ingredient by name.
+ **Responsive Design:** Fully functional on both desktop and mobile devices.
_____________
## Technologies Used
+ **Backend:** Python, Django
+ **Frontend:** HTML5, CSS3, JavaScript
+ **Database:** SQLite3
_________________
## Installation
### Prerequisites
1. Python 3.8 or higher
2. SQLite3
_______________________
## Setup
1. Clone the repository:
```
git clone https://github.com/Liliyakhu/desserts-hub.git
cd desserthub
```
2. Create a virtual environment and install dependencies:
```
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
```
3. Set up the database:
```
python manage.py makemigrations
python manage.py migrate
```
4. Create a superuser for admin access:
```
python manage.py createsuperuser
```
5. Run the development server:
```
python manage.py runserver
```
6. Open your browser and navigate to http://127.0.0.1:8000.
__________________________
## Usage
+ Ask existing user to create your account and log in with your credentials.
+ Browse recipes by category or search for specific desserts.
+ Submit your own desserts through the "Create Dessert" feature.

## Screenshots
### Sign in page:
![Screenshot.](../blob/main/assets/images/Screenshot from 2024-12-04 22-50-13.png?raw=true)
### Home page:

### Dessert page:

