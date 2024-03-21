from flask_testing import TestCase
from flask import current_app, url_for
from main import app


class Main_test(TestCase):
  # Configuración del entorno de pruebas
  def create_app(self):
    app.config["TESTING"]=True
    app.config["WTF_CSRF_ENABLED"]=False
    return app
  
  # Función para probar que la app exista
  def test_app_exists_web(self):
    self.assertIsNotNone(current_app)

  # Probar que la app esté en el ambiente de pruebas
  def test_app_in_testing_mode(self):
    self.assertTrue(current_app.config["TESTING"])

  # Probar los redirects
  def test_index_redirects(self):
    response=self.client.get(url_for("index"))
    self.assertRedirects(response,url_for("show_information"))

  # Probar que el endpoint el metodo get funciona
  def test_show_information_get(self):
    response=self.client.get(url_for("show_information"))
    self.assert200(response)

  
  # Probar los post del endpoint
  # En este caso se envía información, generalmente los datos se envían en formato json
  def test_show_information_post(self):
    test_form_fake={
      "username":"Sebastian",
      "password":"1234**"
    }
    response=self.client.post(url_for("show_information"),data=test_form_fake)

    self.assertRedirects(response, url_for("index"))
    # self.assertRedirects(response,url_for("index"))

  