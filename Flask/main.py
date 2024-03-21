from flask import Flask,request,make_response,redirect,render_template,session,url_for,flash
from flask_bootstrap import Bootstrap
from flask_wtf  import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired
import unittest

app =Flask(__name__)
# app.config["SERVER_NAME"] = "localhost:9999"
bootstrap=Bootstrap(app)
app.config["SECRET_KEY"]='CLAVE SEGURA'

items=["arroz","huevos","café","leche"]

class LogginForm(FlaskForm):
  username= StringField("Nombre del usuario",validators=[DataRequired()])
  password= PasswordField("Contraseña",validators=[DataRequired()])
  submit= SubmitField("Enviar Datos")

@app.cli.command()
def test():
  tests=unittest.TestLoader().discover("tests")
  unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found_endpoint(error):
  return render_template('404.html',error=error)

# Indicamos la ruta
@app.route("/index")
def index():
  user_ip_info=request.remote_addr
  #response=make_response(redirect("/show_information_address"))
  response=redirect(url_for("show_information",_external=True))
  #response.set_cookie("user_ip_info",user_ip_info)
  session["user_ip"]=user_ip_info
  return response
  # return f"Hola mundo, tu dirección ip es la siguiente {user_ip_info}"


@app.route("/show_information_address", methods=["GET","POST"])
def show_information():
  # user_ip=request.cookies.get("user_ip_info")
  user_ip=session.get("user_ip")
  username=session.get("username")
  login_form=LogginForm()
  context={
    "user_ip":user_ip,
    "items":items,
    "login_form":login_form,
    "username":username
  }

  if login_form.validate_on_submit():
    username=login_form.username.data
    session["username"]=username
    flash("Nombre de usuario registrado correctamente")
    return redirect(url_for("index",_external=True))

  return render_template("ip_information.html",**context)
  # return f"Hola mundo, tu dirección ip es la siguiente {user_ip}"

# Para correr el código
if __name__=="__main__":
  app.run(host="0.0.0.0",port=9999,debug=True)
  # app.run(debug=True)