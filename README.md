Play Beat
-----

## Introduction

Play Beat is a musical venue and artist booking site that facilitates the discovery and bookings of shows between local performing artists and venues. This site lets you list new artists and venues, discover them, and list shows with artists as a venue owner.


It implements various data models to power the API endpoints connects it to a PostgreSQL database for storing, querying, and creating information about artists and venues .

## Overview

This web app attempts at achieving the following:

* creating new venues, artists, and creating new shows.
* searching for venues and artists.
* learning more about a specific artist or venue.

Play Beat is the next platform that artists and musical venues can use to find each other, and discover new music shows.

![play_beat-1](https://user-images.githubusercontent.com/71264542/155092469-9b84f10c-943c-477d-907c-dd0ec2bd9f6b.png)

![play-beat-2](https://user-images.githubusercontent.com/71264542/155092509-80328763-c51f-4d1c-9661-c34fba808184.png)

![play-beat-3](https://user-images.githubusercontent.com/71264542/155092536-9972d5bc-d31f-44e6-ab65-ca06d91c76e4.png)
![play-beat-4](https://user-images.githubusercontent.com/71264542/155092580-88323fd5-13ea-438f-9992-fb015180af76.png)


## Tech Stack (Dependencies)

### 1. Backend Dependencies
Our tech stack will include the following:
 * **virtualenv** as a tool to create isolated Python environments
 * **SQLAlchemy ORM** to be our ORM library of choice
 * **PostgreSQL** as our database of choice
 * **Python3** and **Flask** as our server language and server framework
 * **Flask-Migrate** for creating and running schema migrations
 

### 2. Frontend Dependencies
* **HTML**
* **CSS**
* **Javascript**
* **Bootstrap 3**

## Main Files: Project Structure

  ```sh
  ├── README.md
  ├── app.py *** the main driver of the app. Includes your SQLAlchemy models.
                    "python app.py" to run after installing dependencies
  ├── config.py 
  ├── error.log
  ├── forms.py 
  ├── requirements.txt 
  ├── static
  │   ├── css 
  │   ├── font
  │   ├── ico
  │   ├── img
  │   └── js
  └── templates
      ├── errors
      ├── forms
      ├── layouts
      └── pages
  ```

Overall:
* Models are located in the `MODELS` section of `app.py`.
* Controllers are also located in `app.py`.
* The web frontend is located in `templates/`, which builds static assets deployed to the web server at `static/`.
* Web forms for creating data are located in `form.py`




###Implementations
-----

1. Connects to a local database defined in `config.py`.
2. Using SQLAlchemy it sets up noramlized models for the objects defined in the `models.py`,
3. Implements model properties and relationships using database migrations via Flask-Migrate.
3. Implements form submissions for creating new Venues, new Artists and Shows.Establishes proper key constraints in the database to avoid          duplicate or nonsensical form submissions.  
4. Implements the following endpoints:

## Endpoints

## Venues

### `GET /venues`

- Fetches all the venues from the database
- Request arguments: None
- Returns: A list of venues filtered by cities and states




### `GET /venues/<int:venue_id>`

- Fetches a venue matching the venue id
- Request arguments: Venue id
- Returns: a fully detailed venue or `404 Not Found` if there's no venue matching that id 



### `POST /venues/search`

- Fetches venues matching the search term
- Request arguments: Search term
- Returns: A list of venues matches the search term



### `POST /venues/create`

- Creates a venue using the form values
- Request arguments: Venue Form data
- Returns: back to home




### `DELETE /venues/<int:venue_id>`

- Deletes a venue matching the venue id
- Request arguments: Venue id
- Returns: back to home

## Artists

### `GET /artists`

- Fetches all the artists from the database
- Request arguments: None
- Returns: A list of artists



### `GET /artists/<int:artist_id>`

- Fetches an artist matching the artist id
- Request arguments: None
- Returns: an artist matching the artist id or `404 Not Found` if there's no artist matching that id 



### `POST /artists/search`

- Fetches artists matching the search term
- Request arguments: Search term
- Returns: A list of artists matches the search term



### `POST /artists/create`

- Creates an artist using the form values
- Request arguments: Artist Form data
- Returns: back to home


### Shows 



### `POST /shows/create`

- Creates a show using the form data
- Request arguments: Show Form data
- Returns: back to home





## Development Setup
1. **Download the project starter code locally**
```
git clone https://github.com/udacity/FSND.git
cd FSND/projects/01_Play Beat/starter_code 
```

2. **Create an empty repository in your Github account online. To change the remote repository path in your local repository, use the commands below:**
```
git remote -v 
git remote remove origin 
git remote add origin <https://github.com/<USERNAME>/<REPO_NAME>.git>
git branch -M master
```
Once you have finished editing your code, you can push the local repository to your Github account using the following commands.
```
git add . --all   
git commit -m "your comment"
git push -u origin master
```

3. **Initialize and activate a virtualenv using:**
```
python -m virtualenv env
source env/bin/activate
```
>**Note** - In Windows, the `env` does not have a `bin` directory. Therefore, you'd use the analogous command shown below:
```
source env/Scripts/activate
```

4. **Install the dependencies:**
```
pip install -r requirements.txt
```

5. **Run the development server:**
```
export FLASK_APP=myapp
export FLASK_ENV=development # enables debug mode
python3 app.py
```

6. **Verify on the Browser**<br>
Navigate to project homepage [http://127.0.0.1:5000/](http://127.0.0.1:5000/) or [http://localhost:5000](http://localhost:5000) 



## Deployment
This app is deployed on Heroku. For deployment, you need to:

1. Install Heroku CLI and login to Heroku on the terminal

2. create a [setup.sh](setup.sh) file and declare all your variables in the file

3. Install gunicorn
``` bash
    pip install gunicorn
```

4. Create a [Procfile](Procfile) and add the line below. The Procfile instructs Heroku on what to do. Make sure that **your app** is housed in **[app.py](app.py)**
``` bash
    web: gunicorn app:app
```

5. Install the following requirements
``` bash
    pip install flask_script
    pip install flask_migrate
    pip install psycopg2-binary
```       

6. Freeze your requirements in the [requirements.txt](requirements.txt) file
``` bash
    pip freeze > requirements.txt
```   

7. Create Heroku app
``` bash
    heroku create name_of_your_app
```
        
8. Add git remote for Heroku to local repository
``` bash
    git remote add heroku heroku_git_url
``` 

9. Add postgresql add on for our database
``` bash
    heroku addons:create heroku-postgresql:hobby-dev --app name_of_your_application
```
10. Add all the Variables in Heroku under settings
``` bash
    # This should already exist from the last step
    DATABASE_URL
    # Get these from Auth0
    AUTH0_DOMAIN
    ALGORITHMS
    API_AUDIENCE
```
        
10. Push any changes to your GitHub Repository

11. Push to Heroku
``` bash
    git push heroku master
```      

12. Run Migrations to the Heroku database
``` bash
    heroku run python manage.py db upgrade --app name_of_your_application
```

Heroku app hosted at https://beat-playzz.herokuapp.com/
