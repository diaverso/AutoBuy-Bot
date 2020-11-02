from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import keys
import threading
import time
import smtplib

def timeme(method):
    def wrapper(*args, **kw):
        startTime = int(round(time.time() * 1000))
        result = method(*args, **kw)
        endTime = int(round(time.time() * 1000))
        print((endTime - startTime)/1000, 's')
        return result
    return wrapper

# will cookies improve load time?
options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=www.pccomponentes.com')

@timeme
def order():
    # Añadir al Carro
    driver.find_element_by_xpath('//*[@id="btnsWishAddBuy"]/button[3]').click()
    driver.implicitly_wait(20)
    driver.find_element_by_xpath('//*[@id="GTM-carrito-realizarPedidoPaso1"]').click()
    # Iniciar Sesion
    time.sleep(0.3)
    driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/div/input').send_keys(keys['email'])
    time.sleep(0.2)
    driver.find_element_by_xpath('//*[@id="login-form"]/div[5]/div/div/input').send_keys(keys['pass'])
    driver.find_element_by_xpath('//*[@id="login-form"]/button[2]/div').click()

    # Finalizar compra
    # - Selecionamos el metodo de pago (Trasferencia Bancaria)
    driver.find_element_by_xpath('//*[@id="formPaymentTypes"]/div[3]/label/span[1]').click()
    time.sleep(3.2)
    driver.find_element_by_xpath('//*[@id="ticket-pago"]/p/label/span').click()
    driver.find_element_by_xpath('//*[@id="GTM-carrito-finalizarCompra"]').click()


    # Enviar Correo
    message = 'Felicidades, Se completo la compra!'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('correo', 'contraseña')

    server.sendmail('correoenvio', 'correorecepcion', message)
    server.quit()

if __name__ == '__main__':
        # load chrome
    driver = webdriver.Chrome('./chromedriver')

    # get product url
    driver.get(keys['product_url'])
    order()