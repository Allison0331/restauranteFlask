import os 
import os.path
from flask import Flask , render_template , redirect , request , url_for , before_render_template, after_this_request
from werkzeug.utils import secure_filename
from forms.forms import LoginForm, ProductForm, RegistroForm
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
<<<<<<< HEAD

import easygui as eg
=======
>>>>>>> 85780e013a170f646ee37316bfec677f55929e6e
import sqlite3
from sqlite3 import Error
from db import *

UPLOAD_FOLDER = os.path.abspath("app/static/imagenes/products") 
ALLOWED_EXTENSIONS = set(["png","jpg","jpeg"])

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/ingresar', methods=['GET', 'POST'])
def ingresar():
    form= LoginForm()
    if request.method == 'POST':
        usuario=request.form['usuario']
        contrasena=request.form['contrasena']
        #usuario=form.usuario.data
        #contrasena=form.contrasena.data
        db = get_db()
        cursorObj = db.cursor()
        cursorObj.execute('SELECT * FROM usuarios WHERE nombre_usuario = ? and contrasena = ?' ,(usuario, contrasena))
        loginusuarios=cursorObj.fetchall()
        session['user']=usuario
        if len(loginusuarios)>0:
            if(session['user']== 'Admin'):
                return redirect(url_for('Admin'))
            else:
                return redirect(url_for('perfilUser'))
        else:
            flash('Usuario o contraseña incorrecta','warning')
            return redirect(url_for('ingresar'))        
    return render_template('ingresar.html', form=form)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('ingresar'))


@app.route('/registro_usuario')
<<<<<<< HEAD
def registro_usuario():

=======
def registro_usuario():    
>>>>>>> 85780e013a170f646ee37316bfec677f55929e6e
    return render_template('registro.html')

""" RUTAS PARA EL DASHBOARD ADMINISTRATIVO """

@app.route('/Admin')
def Admin():
    if ('user' in session and session['user']=='Admin'):
        return render_template('dashAdministrativo.html')
    return redirect (url_for('errorAcceso'))

@app.route('/dashUser3')
def dashUser3():
<<<<<<< HEAD
    
    
    try:

        conexion = sqlite3.connect('restaurante.db')

        print("Connection is established: Database is created in memory")

        cursorObj = conexion.cursor()

        cursorObj.execute('SELECT * FROM productos')

        rows = cursorObj.fetchall()

    except Error:

        print(Error)

    finally:

        conexion.close()
=======
    if ('user' in session and session['user']=='Admin') :    
        sql = 'SELECT * FROM usuarios'
        con = connectar()
        consul = consultar(sql)
        rows = consul.fetchall()
        con.close()
>>>>>>> 85780e013a170f646ee37316bfec677f55929e6e
        
        """rows = cursorObj.fetchall()"""           
                
        return render_template('dashUser3.html',rows = rows)
    return redirect (url_for('errorAcceso'))
    

@app.route('/regDashUser')
def regDashUser():
    if ('user' in session and session['user']=='Admin'):
        return render_template('registrarDashUser.html')
    return redirect (url_for('errorAcceso'))
    

@app.route('/layout')
def layout():
    return render_template('layoutDashboard.html')

@app.route('/errorAcceso')
def errorAcceso():
    session.clear()
    return render_template('errorAcceso.html')

@app.route('/enConstruccion')
def enConstruccion():
    session.clear()
    return render_template('enConstruccion.html')


@app.route('/platos')
def platos():
<<<<<<< HEAD
    return render_template('dashPlatos3.html') 
=======
    if ('user' in session and session['user']=='Admin'):   
        sql = 'SELECT * FROM productos'
        con = connectar()
        consul = consultar(sql)
        rows = consul.fetchall()
        con.close()
        
        return render_template('dashPlatos3.html', rows = rows)
    return redirect (url_for('errorAcceso'))
      
>>>>>>> 85780e013a170f646ee37316bfec677f55929e6e

"""RUTAS DEL PERFIL DE USUARIO"""
@app.route('/perfilUser')
def perfilUser():
    if ('user' in session):
        return render_template('editar_perfil.html')
    return redirect (url_for('errorAcceso'))

@app.route('/lista_deseos')
def lista_deseos():
    if 'user' in session:
        return render_template('listaDeseos.html')
    return redirect (url_for('errorAcceso'))
    

@app.route('/editar_perfil')
def editar_perfil():
    if 'user' in session:
        return render_template('editarPerfilUsuario.html')
    return redirect (url_for('errorAcceso'))


@app.route('/pedidos')
def pedidos():
    if 'user' in session:
        return render_template('pedidos.html')
    return redirect (url_for('errorAcceso'))


""""""

<<<<<<< HEAD
@app.route('/iniciar_sesion' , methods = ['POST'])
def iniciar_sesion():
    nombreUser = request.form['nombreUser']
    if nombreUser == "admin":
        return Admin()
    else:
        return render_template('editar_perfil.html')
    

   
=======
>>>>>>> 85780e013a170f646ee37316bfec677f55929e6e

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
    return render_template('/menuBebidas.html')

@app.route('/platos/nuevo', methods=['GET','POST'])
def addProduct():
    if ('user' in session and session['user']=='Admin'):
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
    return redirect (url_for('errorAcceso'))


"""RUTAS PARA EL MANEJO DE LA BASE DE DATOS BACK-END"""
<<<<<<< HEAD
@app.route('/crear_usuario' , methods =('GET' , 'POST'))
def crear_usuario(codigo):
    codigousuario = codigo
    return "Crear Usuario"
=======
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
    
>>>>>>> 85780e013a170f646ee37316bfec677f55929e6e

@app.route('/Modificar_usuario' , methods =('GET' , 'POST'))
def modificar_usuario(codigo):
    if ('user' in session and session['user']=='Admin'):
        codigousuario = codigo
        return "Modificar Usuario"
    return redirect (url_for('errorAcceso'))

@app.route('/Consultar_usuarios' , methods =('GET' , 'POST'))
def consultar_usuarios():
    if ('user' in session and session['user']=='Admin'):
        return "Consultar Usuarios"
    return redirect (url_for('errorAcceso'))



if __name__ == '__main__':
    app.run(debug=True)    