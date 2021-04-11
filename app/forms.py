from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from wtforms import validators


class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    submit = SubmitField('Iniciar sesión')


class TodoForm(FlaskForm):
    description = StringField('Añade nueva tarea', validators=[DataRequired()])
    submit = SubmitField('Crear')


class DeleteTodoForm(FlaskForm):
    submit = SubmitField('Borrar')


class UpdateTodoForm(FlaskForm):
    submit = SubmitField('Completado')
