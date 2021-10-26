from flask import Flask , flash, session, render_template , redirect , request , url_for , before_render_template, after_this_request
import os 
import os.path
from flask import Flask , render_template , redirect , request , url_for , before_render_template, after_this_request
from werkzeug.utils import secure_filename
from forms.forms import LoginForm, ProductForm, RegistroForm
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField

import sqlite3
from sqlite3 import Error
from db import *

UPLOAD_FOLDER = os.path.abspath("app/static/imagenes/products") 
ALLOWED_EXTENSIONS = set(["png","jpg","jpeg"])

from modelo.conexion import *



app = Flask(__name__)
app.secret_key = 'app secret key'
app.secret_key = os.urandom(24)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route('/')
def index():
    
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    
    return render_template('home.html')
    

@app.route('/ingresar')
def ingresar():
    return render_template('ingresar.html')


@app.route('/registro_usuario')
def registro_usuario():
    
    return render_template('registro.html')

""" RUTAS PARA EL DASHBOARD ADMINISTRATIVO """

@app.route('/Admin')
def Admin():
    return render_template('dashAdministrativo.html')

@app.route('/dashUser3')
def dashUser3():
    sql = 'SELECT * FROM usuarios'
    con = connectar()
    consul = consultar(sql)
    rows = consul.fetchall()
    con.close()
    
    """rows = cursorObj.fetchall()"""
        
            
    return render_template('dashUser3.html',rows = rows)
    

@app.route('/regDashUser')
def regDashUser():
    return render_template('registrarDashUser.html')

@app.route('/layout')
def layout():
    return render_template('layoutDashboard.html')

@app.route('/platos')
def platos():
    sql = 'SELECT * FROM productos'
    con = connectar()
    consul = consultar(sql)
    rows = consul.fetchall()
    con.close()
    
    return render_template('dashPlatos3.html', rows = rows)  

"""RUTAS DEL PERFIL DE USUARIO"""
@app.route('/editar_perfil')
def perfil():
    return render_template('editar_perfil.html')

@app.route('/lista_deseos')
def lista_deseos():
    return render_template('listaDeseos.html')

@app.route('/perfil_usuario/editar_perfil')
def editar_perfil():
    return render_template('editarPerfilUsuario.html')


@app.route('/pedidos')
def pedidos():
    return render_template('pedidos.html')


""""""

@app.route('/iniciar_sesion' , methods = ['POST'])
def iniciar_sesion():
    nombreUser = request.form['nombreUser']
    
    if nombreUser == "admin":
        return Admin()
    else:
        
        return render_template('editar_perfil.html')
    

   

@app.route('/menu')
def menu():
    return render_template('menu.html')


@app.route('/menu/horneados')
def menu_horneados():
    return render_template('menuHorneados.html')


@app.route('/menu/desayunos')
def menu_desayunos():
    return render_template('menuDesayunos.html')


@app.route('/menu/bebidas')
def menu_bebidas():
    return render_template('menuBebidas.html')

@app.route('/platos/nuevo', methods=['GET','POST'])
def addProduct():
    form = ProductForm()
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        categoria = request.form['categoria']
        precio = request.form['precio']
        cantidad = request.form['precio']
        imagen = request.files['imagen']
        filename = secure_filename(imagen.filename)
        imagen.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        estado = request.form['estado']
        
        db = get_db()
        db.execute('INSERT INTO productos(nombre, descripcion, categoria, valor_unitario, cantidad, url, estado) VALUES (?,?,?,?,?,?,?)', (nombre,descripcion,categoria, precio,cantidad, filename, estado) )
        db.commit()
        return redirect(url_for("platos", respuesta='success'))
    return render_template('dashPlatosNuevo.html',form=form)


"""RUTAS PARA EL MANEJO DE LA BASE DE DATOS BACK-END"""
@app.route('/crear_usuario' , methods=['GET', 'POST'])
def crear_usuario():
    if request.method == 'POST':
        tipo = request.form['tipo']
        documento = request.form['documento']
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        fecha = request.form['fecha']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        email = request.form['email']
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        nivel = 3
        estado = True
        
        
        try:
            con = connectar()
            sql = 'INSERT INTO usuarios(tipo_identificacion, identificacion, nombres, apellidos, fecha_nacimiento, direccion, telefono, email, nombre_usuario, contrasena, nivel_acceso, estado) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
            entities = (tipo, documento, nombres, apellidos, fecha, direccion, telefono, email, usuario, contrasena, nivel, estado)

            insertar(sql, entities)
            
            flash('Registro creado con exito', 'success')
            
            return redirect( url_for('ingresar') )
               
        except Error:
            print(Error)
        
        con.close()
    else:
        return render_template('home.html')
    

@app.route('/Modificar_usuario' , methods =('GET' , 'POST'))
def modificar_usuario(codigo):
    codigousuario = codigo
    return "Modificar Usuario"

@app.route('/Consultar_usuarios' , methods =('GET' , 'POST'))
def consultar_usuarios():
    return "Consultar Usuarios"



if __name__ == '__main__':
    app.run(debug=True)
    