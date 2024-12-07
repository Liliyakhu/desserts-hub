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
![Screenshot.](https://private-user-images.githubusercontent.com/49777953/392569820-c4de94e1-47e6-4aef-a841-a40e01c3d2b6.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzM2MDEyMTcsIm5iZiI6MTczMzYwMDkxNywicGF0aCI6Ii80OTc3Nzk1My8zOTI1Njk4MjAtYzRkZTk0ZTEtNDdlNi00YWVmLWE4NDEtYTQwZTAxYzNkMmI2LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDEyMDclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMjA3VDE5NDgzN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTc3ZGFjOWQyNTZkODVlNTM0MTQxYTZkNWIyZGFiNjY1NzZhM2FkYjUwOTc5ZjRhZDlkMzU3NmM0NDZiNGIyZDAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.d1jiH-mgV5ohQpix0S54xndyAIpPIYraCe0kqUACNCQ)
### Home page:

### Dessert page:

