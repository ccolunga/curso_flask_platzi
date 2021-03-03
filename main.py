from flask import Flask, request, make_response, redirect render_tamplate

app = Flask(__name__)

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

@app.route("/hello")
def hello():
    user_ip = request.cookies.get("user_ip")
    # ''' el uso de {}.format() es para mostrar '''
    return "Hello world Flask, tu ip es {}".format(user_ip)
