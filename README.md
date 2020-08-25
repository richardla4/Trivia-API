# Trivia API

This project is a web application that uses a webpage to manage the trivia data and play the trivia game.

This app allows users to:
    1. Display questions - all or by category. Questions also show category and difficulty, and users can show/hide the answer
    2. Delete questions
    3. Add questions with category and difficulty
    4. Search for questions based on a text query string
    5. Play the trivia game, randomizing all questions or within a specific category

## Game Play Mechanics

Currently, when a user plays the game they play up to five questions of the chosen category. If there are fewer than five questions in a category, the game will end when there are no more questions in that category. 

## About the Stack

### Backend

The `./backend` directory contains a completed Flask and SQLAlchemy server. The Trivia API endpoints are defined in ```__init__.py``` file and references ```models.py``` for database and SQLAlchemy setup. 

All backend code follows [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/). 

### Frontend

The `./frontend` directory contains a complete React frontend to consume the data from the Flask server. 

## Getting Started

### Installing Dependencies

Developers using this project should already have Python3, pip and node installed on their local machines.

#### Virtual Environment

Working within a virtual environment is recommended

#### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is utilized in this project to build a simple web server to handle the API requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM that is used to interact and interface with the PostgreSQL database.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension used to handle cross origin requests to the API.

#### Backend Dependencies

Navigate to the backend directory and run:

```
pip install -r requirements.txt
```

This installs all the required packages included in the `requirements.txt` file.

#### Frontend Dependencies

Navigate to the frontend directory and run:

```
npm install
```

This install all the dependencies defined in the package.json file

## Database Setup

With Postgres running, restore a database using the `trivia.psql` file. Navigate to the backend directory and run:
```
createdb trivia
psql trivia < trivia.psql
```

## Running the server

From within the backend directory, run the following commands:
```
export FLASK_APP=flaskr
eport FLASK_ENV=development
flask run
```

These commands put the application in development and directs our application to use the `__init__.py` file in our flaskr folder. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made. If running locally on Windows, look for the commands in the [Flask documentation](http://flask.pocoo.org/docs/1.0/tutorial/factory/).

The application is run on `http://127.0.0.1:5000/` by default and is a proxy in the frontend configuration. 

## Running the REACT frontend

From within the frontend directory, run the following to start the client:
```
npm start
```

The frontend app was built using create-react-app. ```npm start``` runs the app in development mode, this can be changed in the ```package.json``` file.

By default, the frontend will run on `http://127.0.0.1:3000/`

## Testing
In order to run tests, navigate to the backend folder and run:

```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

The first time you run the tests, omit the dropdb command

All tests are kept in ```test_flaskr.py``` and it should be maintained as updates are made to app functionality.

## API Reference

### Getting Started
- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration. 
- Authentication: This version of the application does not require authentication of API keys.

### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    'success': False,
    'error': 400,
    'message': 'Bad request'
}
```

The API will return four error types when requests fail:
- 400: Bad request
- 404: Resource not found
- 422: Unprocessable entity
- 500: Internal server error

### Endpoints

#### GET /categories
- General:
    - Returns all the categories and success value

- Sample: `curl http://127.0.0.1:5000/categories`
```
{
    'success': True,
    'categories': {
        '1': 'Science',
        '2': 'Art',
        '3': 'Geography',
        '4': 'History',
        '5': 'Entertainment',
        '6': 'Sports'
    }
}
```

#### GET /questions
- General:
    - Returns all questions, categories, success value, and total number of questions
    - Results are paginated in groups of 10. Optionally, include a request argument to choose page number, starting from 1.
- Sample: `curl http://127.0.0.1:5000/questions`
```
{
    'success': True,
    'categories': {
        '1': 'Science',
        '2': 'Art',
        '3': 'Geography',
        '4': 'History',
        '5': 'Entertainment',
        '6': 'Sports'
    },
    [
        {
            'answer': 'Tom Cruise',
            'category': 5,
            'difficulty': 4,
            'id': 4,
            'question': 'What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?'
        },
        {
            'answer': 'Maya Angelou',
            'category': 4,
            'difficulty': 2,
            'id': 5,
            'question': 'Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?'
        },
        {
            'answer': 'Edward Scissorhands',
            'category': 5,
            'difficulty': 3,
            'id': 6,
            'question': 'What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?'
        },
        {
            'answer': 'Muhammad Ali',
            'category': 4,
            'difficulty': 1,
            'id': 9,
            'question': 'What boxer's original name is Cassius Clay?'
        },
        {
            'answer': 'Brazil',
            'category': 6,
            'difficulty': 3,
            'id': 10,
            'question': 'Which is the only team to play in every soccer World Cup tournament?'
        },
        {
            'answer': 'Uruguay',
            'category': 6,
            'difficulty': 4,
            'id': 11,
            'question': 'Which country won the first ever soccer World Cup in 1930?'
        },
        {
            'answer': 'George Washington Carver',
            'category': 4,
            'difficulty': 2,
            'id': 12,
            'question': 'Who invented Peanut Butter?'
        },
        {
            'answer': 'Lake Victoria',
            'category': 3,
            'difficulty': 2,
            'id': 13,
            'question': 'What is the largest lake in Africa?'
        },
        {
            'answer': 'The Palace of Versailles',
            'category': 3,
            'difficulty': 3,
            'id': 14,
            'question': 'In which royal palace would you find the Hall of Mirrors?'
        },
        {
            'answer': 'Agra',
            'category': 3,
            'difficulty': 2,
            'id': 15,
            'question': 'The Taj Mahal is located in which Indian city?'
        }
    ],
    'total_questions': 19
}
```

#### DELETE /questions/{int:question_id}
- General:
    - Deletes a question of the given question_id if it exists. Returns success value and message.
- Sample: `curl -X DELETE http://127.0.0.1:5000/questions/6`
```
{
    'success': True,
    'message': 'Question successfully deleted'
}
```

#### POST /questions
- General:
    - Creates a new question using the submitted question, answer, category, and difficulty. Returns success value and message.
- Sample: `curl http://127.0.0.1:5000/questions -X POST -H 'Content-Type: application/json' -d '{'question': 'Frankie Fredericks represented which African country in athletics?', 'answer': 'Namibia', 'difficulty': 3, 'category': '6'}'`
```
{
    'success': True,
    'message': 'Question successfully posted'
}
```

#### POST /questions/search
- General:
    - Returns all questions that contain the search query string
    - Also returns success value and total number of questions that the search returned
    - Results are paginated in groups of 10. Optionally, include a request argument to choose page number, starting from 1.
- Sample: `curl http://127.0.0.1:5000/questions/search -X POST -H 'Content-Type: application/json' -d '{'searchTerm': 'lake'}'`
```
{
    'success': True,
    'questions': [
        {
            'question': 'What is the largest lake in Africa?',
            'answer': 'Lake Victoria',
            'difficulty': 2,
            'category': 3
        }
    ],
    'total_questions': 1
}
```

#### GET /categories/{int:category_id}/questions
- General:
    - Returns questions by category using category_id, if it exists
    - Also returns success value, current category, and total number of questions in the current category
    - Results are paginated in groups of 10. Optionally, include a request argument to choose page number, starting from 1.
- Sample: `curl http://127.0.0.1:5000/categories/1/questions`
```
{
    'success': True,
    'questions':  [
        {
        'answer': 'The Liver',
        'category': 1,
        'difficulty': 4,
        'id': 20,
        'question': 'What is the heaviest organ in the human body?'
        },
        {
        'answer': 'Alexander Fleming',
        'category': 1,
        'difficulty': 3,
        'id': 21,
        'question': 'Who discovered penicillin?'
        },
        {
        'answer': 'Blood',
        'category': 1,
        'difficulty': 4,
        'id': 22,
        'question': 'Hematology is a branch of medicine involving the study of what?'
        }
    ],
    'total_questions': 3,
    'current_category': 'Science'
}
```

#### POST /quizzes
- General:
    - Takes category and previous questions from the request
    - Returns success value and random question within given category that does not exist within previous questions
- Sample: `curl http://127.0.0.1:5000/quizzes -X POST -H 'Content-Type: application/json' -d '{'previous_questions': [5, 9], 'quiz_category': {'type': 'History', 'id': '4'}}'`
```
{
    'success': True,
    'question': {
        'answer': 'George Washington Carver',
        'category': 4,
        'difficulty': 2,
        'id': 12,
        'question': 'Who invented Peanut Butter?'
    }
}
```
