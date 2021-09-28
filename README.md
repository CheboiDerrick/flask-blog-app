# MY Word

## By [Derrick Cheboi](https://github.com/CheboiDerrick/)

## Description
My Word is a web application that enables users to share blog post with each other. Users can add comments to other users blog posts and like or dislike them.



## Application Behaviour
These are the behaviours/features that the application implements for use by a user.

A user should be able to:
* View the blog posts on the site
* Comment on blog posts
*  View the most recent posts
*  Email alert when a new post is made by joining a subscription.
*  See random quotes on the site
* Sign in to the blog.
* Ceate a blog from the application.
* Delete comments that I find insulting or degrading.
* Update or delete blogs I have created.


## SetUp / Installation Requirements
### Prerequisites
* python3.8
* pip3
* pipenv
* Git and Github

### Cloning
* In your terminal:
        
        $ git clone https://github.com/CheboiDerrick/flask-blog-app.git
        $ cd pitch-app

## Running the Application
* Install the requirements:

         $ pipenv install

* Start your virtual environmrnt;

        $ pipenv shell 

* Export your configuraions

        $ export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}

        $ export SECRET_KEY='Your secret key'

        $ export MAIL_USERNAME='Your email username'

        $ export MAIL_PASSWORD='Your password'

* To run the application, in your terminal:
        
        $ python3.8 manage.py server
    

* Open your browser and navigate to http://localhost:5000 to view the web app

        
## Technologies and Languages Used
* Python -(3.8)
* Flask


## License
[MIT](https://github.com/CheboiDerrick/flask-blog-app/blob/main/LICENCE) 

&copy;2021