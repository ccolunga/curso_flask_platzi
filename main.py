from flask import request, make_response, redirect, render_template, session, url_for, flash
import unittest

from app.firestore_service import get_users
from app.firestore_service import get_todos
from app import create_app
#from app.forms import LoginForm

app = create_app()

todos = ['Comprar cafe', 'Enviar solicitud de compra',
         'Entregar video a producto']

# Los decoradores que usen route se les llama vistas


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def not_found(error):
    return render_template('500.html', error=error)


@app.route("/")
def index():
    #raise(Exception('500 error'))
    user_ip = request.remote_addr

    response = make_response(redirect("/hello"))
    #response.set_cookie("user_ip", user_ip)
    session['user_ip'] = user_ip
    return response


@app.route("/hello", methods=['GET'])
def hello():
    user_ip = session.get("user_ip")
    username = session.get('username')

    context = {
        'user_ip': user_ip,
        'todos': get_todos(user_id=username),
        'username': username
    }

    users = get_users()
    # print(users)
    for user in users:
        print(user.id)
        print(user.to_dict()['password'])

    return render_template("hello.html", **context)
