from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

todos = ['TODO 1', 'TODO 3', 'TODO 3']

# Los decoradores que usen route se les llama vistas


@app.route("/")
def index():
    user_ip = request.remote_addr

    response = make_response(redirect("/hello"))
    response.set_cookie("user_ip", user_ip)

    return response


""" 
Para las routes dinamicas basta con agregar <> por ejemplo

RUTA ESTATICA
@app.route('/hello/<user>')
def helloUser(user):
    return 'Hello {}'.format(user)

RUTA DINAMICA
@app.route('/hello/Cesar')
def helloUser(user):
    return 'Hello {}'.format(user)

"""

""" 
El uso de los 3 asteriscos es para desglosar las variables que se tiene en un dictionario
por ejemplo:

context = {
        'user_ip': user_ip,
        'todos': todos
    }

SIN USAR ASTERISCOS
#RESULTADO 
# {'user_ip': user_ip, 'todos': todos}

USANDO ASTERISCOS
#RESULTADO 
# 'user_ip': user_ip, 'todos': todos
"""


@app.route("/hello")
def hello():
    user_ip = request.cookies.get("user_ip")
    context = {
        'user_ip': user_ip,
        'todos': todos
    }

    return render_template("hello.html", **context)
