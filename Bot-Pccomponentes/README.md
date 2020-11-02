# AutoBuy-Bot
Esto es un repositorio donde se encontraran excripts para hacer bots automaticos para automatizar compras.
El Bot funciona en Python3 y estan testeados en Ubuntu 20.04

# Instalacion
1º Instalamos python3 en ubuntudektop 
  -     sudo apt update
  -     sudo apt -y upgrade
2º Instalamos pip para python3
 - sudo apt install -y python3-pip
3º Instalamos los paqueteces necesarios para que funcione correctamente el script
  - pip3 install selenium==3.14.1
  - pip3 install urllib3==1.24.2
 
 # Configuracion
 1º Abrivos el archivo "config.py" y le añadimos una url entre los parentesis.
  - Ejemplo: "product_url": "https://www.pccomponentes.com/msi-mpg-trident-3-10si-017eu-intel-core-i5-10400-8gb-1tb-512gb-ssd-gtx-1660-super",
  
 2º Añadimos el correo para iniciar sesion:
  - Ejemplo: "email": "pedroytucasa@gmail.com",
  
 3º Añadimos la contraseña :
  - Ejemplo: "pass": "tuynadiemas"
  
  # Configuracion del autocorreoelectronico (Esto te envia un correo electronico cuando se completa la cuenta)
  
    - server.login('correo', 'contraseña') | Se tiene que sustituir el 'correo' por un correo electrnico tuyo de gmail (Puedes crear uno nuevo para solo esto), y en 'contraseña' tienes que poner la contraseña del correo electrnico anteriormente puesta.

    - server.sendmail('correoenvio', 'correorecepcion', message) | Tienes que poner en 'correoenvio' el correo electrnico que pusiste en la configuracion de login, y en 'correorecepcion' es donde se recibira el correo electronico con el mensaje.

    - message = 'Felicidades, Se completo la compra!' | Puedes cambiar el mensaje por el que tu quieras, es lo que aperece de titulo del correo.


# Descargar "chromedriver" Aqui tienes los links para descargarlo, tienes que descargarte la misma version que el navegador que tengas instalado o la mas proxima.
    - Google Chrome Driver: https://chromedriver.chromium.org/downloads
    - Firefox Driver: https://github.com/mozilla/geckodriver/releases