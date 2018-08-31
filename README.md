# tourists

## Installation

    $ git clone git@github.com:manyashka146/tourists.git
    $ cd tourists
    $ python -m venv env
    $ source env/bin/activate
    $ pip install -r requirements.txt
    
Run the migrations:
  
    $ python manage.py migrate
       
Starting server:

    $ python manage.py runserver
    
## How to use

Registration (via httpie):

    $ http POST http://localhost:8000/register/ username="Your_name" email="yourmail@mail.com" first_name="Your_first_name" last_name="Your_last_name" password="your_password"  
    
Get JSON Web Token:

    $ http POST http://localhost:8000/sign_in/ username="Your_name" password="your_password"
    
Add location:

    $ http POST http://localhost:8000/locations/ country="Your_country" city="Your_city" name="Name_of_your_location" description="Your_notes" "Authorization: JWT <your_token>"
    
Check-in in location:

    $ http POST http://localhost:8000/locations/1/visit/ ratio="7" "Authorization: JWT <your_token>"
    
Get some info:

    $ http http://localhost:8000/locations/1/ratio/ "Authorization: JWT <your_token>"
    $ http http://localhost:8000/users/1/ratio/ "Authorization: JWT <your_token>"
