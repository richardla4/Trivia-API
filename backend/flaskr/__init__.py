import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def paginate(request, items, items_per_page):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * items_per_page
    end = start + items_per_page

    formatted_items = [item.format() for item in items]
    current_items = formatted_items[start:end]

    return current_items


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    # Set up CORS. Allow '*' for origins.
    CORS(app, resources={'/': {'origins': '*'}})

    # Use the after_request decorator to set Access-Control-Allow
    @app.after_request
    def after_request(response):
        response.headers.add(
          'Access-Control-Allow-Headers', 'Content-Type,Authorization, true'
          )
        response.headers.add(
          'Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS'
          )
        return response

    # Endpoint to handle GET requests for all available categories.
    @app.route('/categories')
    def get_all_categories():
        try:
            categories = Category.query.order_by(Category.id).all()
            data = {}
            for category in categories:
                data[category.id] = category.type
            return jsonify({
              'success': True,
              'categories': data
            }), 200
        except Exception:
            abort(500)

    # Endpoint to handle GET requests for questions,
    # including pagination (every 10 questions).
    @app.route('/questions')
    def get_questions():
        questions = Question.query.order_by(Question.id).all()
        total_questions = len(questions)
        categories = Category.query.order_by(Category.id).all()

        current_questions = paginate(request, questions, QUESTIONS_PER_PAGE)

        if (len(current_questions) == 0):
            abort(404)

        data = {}
        for category in categories:
            data[category.id] = category.type

        try:
            return jsonify({
              'success': True,
              'questions': current_questions,
              'total_questions': total_questions,
              'categories': data
            }), 200
        except Exception:
            abort(500)

    # Endpoint to DELETE question using a question ID.
    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            question = Question.query.get(question_id)
            question.delete()

            return jsonify({
              'success': True,
              'message': 'Question successfully deleted',
              'question_id': question_id
            })
        except Exception:
            abort(422)

    # Endpoint to POST a new question.
    @app.route('/questions', methods=['POST'])
    def post_question():
        data = request.get_json()

        question = data.get('question', '')
        answer = data.get('answer', '')
        difficulty = data.get('difficulty', '')
        category = data.get('difficulty', '')

        if (
          (question == '') or
          (answer == '') or
          (difficulty == '') or
          (category == '')
          ):
            abort(422)

        try:
            question = Question(
              question=question,
              answer=answer,
              difficulty=difficulty,
              category=category
            )
            question.insert()
            return jsonify({
              'success': True,
              'message': 'Question successfully posted'
            }), 201
        except Exception:
            abort(422)

    # Endpoint to get questions based on a search term.
    @app.route('/questions/search', methods=['POST'])
    def search_questions():
        data = request.get_json()
        search_term = data.get('searchTerm', '')
        if search_term == '':
            abort(422)
        try:
            questions = Question.query.filter(
                Question.question.ilike(f'%{search_term}%')
              ).order_by(Question.id).all()
            total_questions = len(questions)
            if total_questions == 0:
                abort(404)
            current_questions = paginate(
                request, questions, QUESTIONS_PER_PAGE
              )
            return jsonify({
              'success': True,
              'questions': current_questions,
              'total_questions': total_questions
            }), 200
        except Exception:
            abort(404)

    # Endpoint to get questions based on category.
    @app.route('/categories/<int:category_id>/questions')
    def get_questions_by_category(category_id):
        category = Category.query.filter_by(id=category_id).one_or_none()
        if (category is None):
            abort(422)

        questions = Question.query.filter_by(category=category_id).all()
        current_questions = paginate(request, questions, QUESTIONS_PER_PAGE)

        return jsonify({
          'success': True,
          'questions': current_questions,
          'total_questions': len(questions),
          'current_category': category.type
        })

    # Endpoint to get questions to play the quiz.
    @app.route('/quizzes', methods=['POST'])
    def play_quiz():
        data = request.get_json()
        previous_questions = data.get('previous_questions')
        quiz_category = data.get('quiz_category')

        if ((quiz_category is None) or (previous_questions is None)):
            abort(400)

        if (quiz_category['id'] == 0):
            questions = Question.query.all()
        else:
            questions = Question.query.filter_by(
                category=quiz_category['id']
              ).all()

        def random_question():
            return questions[random.randint(0, len(questions)-1)]

        found = True

        while found:
            next_question = random_question()
            if next_question.id not in previous_questions:
                found = False

        return jsonify({
          'success': True,
          'question': next_question.format()
        }), 200

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
          'success': False,
          'error': 400,
          'message': 'Bad request'
        }), 400

    @app.errorhandler(422)
    def unprocessable_entity(error):
        return jsonify({
          'success': False,
          'error': 422,
          'message': 'Unprocessable entity'
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
          'success': False,
          'error': 404,
          'message': 'Resource not found'
        }), 404

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
          'success': False,
          'error': 500,
          'message': 'An internal server error has occurred'
        }), 500

    return app
