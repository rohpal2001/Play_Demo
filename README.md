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

## Tech Stack (Dependencies)

### 1. Backend Dependencies
Our tech stack will include the following:
 * **virtualenv** as a tool to create isolated Python environments
 * **SQLAlchemy ORM** to be our ORM library of choice
 * **PostgreSQL** as our database of choice
 * **Python3** and **Flask** as our server language and server framework
 * **Flask-Migrate** for creating and running schema migrations
You can download and install the dependencies mentioned above using `pip` as:
```
pip install virtualenv
pip install SQLAlchemy
pip install postgres
pip install Flask
pip install Flask-Migrate
```
> **Note** - If we do not mention the specific version of a package, then the default latest stable package will be installed. 

### 2. Frontend Dependencies
You must have the **HTML**, **CSS**, and **Javascript** with [Bootstrap 3](https://getbootstrap.com/docs/3.4/customize/) for our website's frontend. Bootstrap can only be installed by Node Package Manager (NPM). Therefore, if not already, download and install the [Node.js](https://nodejs.org/en/download/). Windows users must run the executable as an Administrator, and restart the computer after installation. After successfully installing the Node, verify the installation as shown below.
```
node -v
npm -v
```
Install [Bootstrap 3](https://getbootstrap.com/docs/3.3/getting-started/) for the website's frontend:
```
npm init -y
npm install bootstrap@3
```


## Main Files: Project Structure

  ```sh
  ├── README.md
  ├── app.py *** the main driver of the app. Includes your SQLAlchemy models.
                    "python app.py" to run after installing dependencies
  ├── config.py *** Database URLs, CSRF generation, etc
  ├── error.log
  ├── forms.py *** Your forms
  ├── requirements.txt *** The dependencies we need to install with "pip3 install -r requirements.txt"
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


Highlight folders:
* `templates/pages` -- (Already complete.) Defines the pages that are rendered to the site. These templates render views based on data passed into the template’s view, in the controllers defined in `app.py`. These pages successfully represent the data to the user, and are already defined for you.
* `templates/layouts` -- (Already complete.) Defines the layout that a page can be contained in to define footer and header code for a given page.
* `templates/forms` -- (Already complete.) Defines the forms used to create new artists, shows, and venues.
* `app.py` -- (Missing functionality.) Defines routes that match the user’s URL, and controllers which handle data and renders views to the user. This is the main file you will be working on to connect to and manipulate the database and render views with data to the user, based on the URL.
* Models in `app.py` -- (Missing functionality.) Defines the data models that set up the database tables.
* `config.py` -- (Missing functionality.) Stores configuration variables and instructions, separate from the main application code. This is where you will need to connect to the database.


###Implementations
-----

1. Connects to a local database defined in `config.py`.
2. Using SQLAlcemy it sets up noramlized models for the objects defined in the `models.py`,
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

