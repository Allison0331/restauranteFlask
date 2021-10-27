from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, PasswordField, BooleanField, FileField
from wtforms.fields.core import SelectField, StringField
from wtforms.fields.html5 import EmailField, IntegerField
from wtforms.validators import DataRequired, EqualTo, InputRequired

class LoginForm(FlaskForm):
    usuario = TextField('Usuario *', validators = [InputRequired(message='Indique el usuario')])
    contrasena = PasswordField('Clave *', validators = [InputRequired(message='Indique la clave')])
    recordar = BooleanField('Recordar Usuario')
    btn = SubmitField('Login')

class RegistroForm(FlaskForm):
    nom = TextField('Nombre *', validators = [InputRequired(message='Indique el nombre')])
    ape = TextField('Apellidos *', validators = [InputRequired(message='Indique el apellido')])
    tel = TextField('Telefono *', validators = [InputRequired(message='Indique el Telefono')])
    dir = TextField('Direccion *', validators = [InputRequired(message='Indique la Dirección')])
    usu = TextField('Usuario *', validators = [InputRequired(message='Indique el usuario')])
    ema = EmailField('Email *', validators = [InputRequired(message='Indique el email')])
    cla = PasswordField('Clave *', validators = [InputRequired(message='Indique la clave')])
    ver = PasswordField('Verificación *', validators = [InputRequired(message='Indique la verificación'), EqualTo(cla,message='Clave y la verificación no coinciden')])
    btn = SubmitField('Registrar')

class ProductForm(FlaskForm):
    codigo = IntegerField('Código', validators=[DataRequired(message="Debes llenar este campo")])
    nombre = TextField('Nombre del producto', validators=[DataRequired(message="Debes llenar este campo")])
    descripcion = TextField('Descripción', validators=[DataRequired(message="Debes llenar este campo")])
    categoria = TextField('Categoria', validators=[DataRequired(message="Debes llenar este campo")])
    precio = IntegerField('Precio', validators=[DataRequired(message="Debes llenar este campo")])
    cantidad = IntegerField('Cantidad', validators=[DataRequired(message="Debes llenar este campo")])
    imagen = FileField('imagen')
    estado = SelectField('Estado', choices= [('Activo', 'Activo'), ('Inactivo','Inactivo')])
    