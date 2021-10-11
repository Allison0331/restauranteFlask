from flask import Flask , render_template , redirect , request , url_for , before_render_template, after_this_request
import easygui as eg


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')
    

@app.route('/ingresar')
def ingresar():
    return render_template('ingresar.html')


@app.route('/registro_usuario')
def registro_usuario():
    return render_template('registro.html')


@app.route('/iniciar_sesion' , methods = ['POST'])
def iniciar_sesion():
    nombreUser = request.form['nombreUser']
    
    return eg.msgbox(msg='Bienvenido' + nombreUser,
          title='Control: msgbox', 
          ok_button='Continuar')
    

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


if __name__ == '__main__':
    app.run(debug=True)
    