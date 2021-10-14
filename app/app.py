from flask import Flask , render_template , redirect , request , url_for , before_render_template, after_this_request
import easygui as eg


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pedidos.html')
    

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
    return render_template('dashUser3.html')

@app.route('/regDashUser')
def regDashUser():
    return render_template('registrarDashUser.html')

@app.route('/layout')
def layout():
    return render_template('layoutDashboard.html')

@app.route('/platos')
def platos():
    return render_template('dashPlatos3.html')  




""" RUTAS PARA EL DASHBOARD ADMINISTRATIVO """

@app.route('/Admin')
def Admin():
    return render_template('dashAdministrativo.html')


@app.route('/dashUser3')
def dashUser3():
    return render_template('dashUser3.html')


@app.route('/regDashUser')
def regDashUser():
    return render_template('registrarDashUser.html')


@app.route('/layout')
def layout():
    return render_template('layoutDashboard.html')


@app.route('/platos')
def platos():
    return render_template('dashPlatos3.html')  


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
    return render_template('/menuBebidas.html')


"""RUTAS PARA EL MANEJO DE LA BASE DE DATOS BACK-END"""
@app.route('/crear_usuario' , methods =('GET' , 'POST'))
def crear_usuario(codigo):
    codigousuario = codigo
    return "Crear Usuario"

@app.route('/Modificar_usuario' , methods =('GET' , 'POST'))
def modificar_usuario(codigo):
    codigousuario = codigo
    return "Modificar Usuario"

@app.route('/Consultar_usuarios' , methods =('GET' , 'POST'))
def consultar_usuarios():
    return "Consultar Usuarios"






if __name__ == '__main__':
    app.run(debug=True)
    