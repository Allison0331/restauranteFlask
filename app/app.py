from flask import Flask , render_template , redirect , request , url_for , before_render_template, after_this_request
import easygui as eg


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/ingresar')
def ingresar():
    return render_template('ingresar.html')

@app.route('/editar_perfil')
def editar_perfil():
    return render_template('editar_perfil.html')

@app.route('/registro_usuario')
def registro_usuario():
    return render_template('registro.html')

@app.route('/iniciar_sesion' , methods = ['POST'])
def iniciar_sesion():
    nombreUser = request.form['nombreUser']
    
    return eg.msgbox(msg='Bienvenido' + nombreUser,
          title='Control: msgbox', 
          ok_button='Continuar')
    


if __name__ == '__main__':
    app.run(debug=True)
    