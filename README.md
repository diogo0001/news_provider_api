# Articles provider API

<<<<<<< HEAD
This project is a basic implementation of an api that provides the articles and their data stored by an admin in the system.<br><br>
This is in the development environment only, and needs to be run by Django runserver.<br><br>
Note: albeidt the project is functional, it's incomplete, and it's still in development.
=======
This project is a basic implementation of an api that provides the articles and their data stored by an admin in the system.
>>>>>>> master

### Admin user

Can insert, update and delete the data and users. (CRUD)

### Regular user

Can see the full content if logged, or just the header if Anonymous.

## Endpoints

- Login API: `/api/login/`
- Sign-up API: `/api/sign-up/`
- Administrator restricted APIs:
  - CRUD `/api/admin/authors/`  
  - CRUD `/api/admin/articles/`
- List article endpoint `/api/articles/` with the following response:

```json
[
  {
    "id": "39df53da-542a-3518-9c19-3568e21644fe",
    "author": {
      "id": "2d460e48-a4fa-370b-a2d0-79f2f601988c",
      "name": "Author Name",
      "photo": "https://picture.url"
    },
    "category": "Category",
    "title": "Article title",
    "summary": "This is a summary of the article"
  },
  ...
]

```
- Article detail endpoint `/api/articles/<slug>` with different responses for anonymous and logged users:

    **Anonymous**
    ```json
    {
      "id": "39df53da-542a-3518-9c19-3568e21644fe",
      "author": {
        "id": "2d460e48-a4fa-370b-a2d0-79f2f601988c",
        "name": "Author Name",
        "photo": "https://picture.url"
      },
      "category": "Category",
      "title": "Article title",
      "summary": "This is a summary of the article",
      "firstParagraph": "This is the first paragraph of this article"
    }
    ```

    **Logged user**
    ```json
    {
      "id": "39df53da-542a-3518-9c19-3568e21644fe",
      "author": {
        "id": "2d460e48-a4fa-370b-a2d0-79f2f601988c",
        "name": "Author Name",
        "photo": "https://picture.url"
      },
      "category": "Category",
      "title": "Article title",
      "summary": "This is a summary of the article",
      "firstParagraph": "This is the first paragraph of this article",
      "body": "Second paragraph</p><p>Third paragraph"
    }
    ```

## Dependencies

### Python dependencies

All the python dependencies are in the requirements.txt. Create a new environment (venv, pipenv, etc) then run the following command (where the requirements.txt file is):

```bash
pip install -r requirements.txt
```

### Database

There are 2 options that you can run this project. 
- With default SqLite database (uncomment the DATABASE list in the settins.py file). 
- With Postgres 13, that's implemented (have to be installed). 

## Running

Execute the following commands in the terminal (where the manage.py file is):

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```