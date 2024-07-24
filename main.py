from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


chromedriver_path = 'C:/Users/Nelso/OneDrive/Documentos/Proyectos/chromedriver-win64/chromedriver.exe'

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")

driver = webdriver.Chrome(
    service=Service(chromedriver_path),
    options=opts
)


#URL Categoria despensa 
driver.get('https://acuenta.cl/ca/despensa/05')
sleep(20)

#Obteniendo Nombre de los Productos
def ObteniendoNombres():
    try:
        nombres = driver.find_elements(By.CLASS_NAME,'prod__name')
        for nombre in nombres:
            print(nombre.text)
    except:
        print("No se pudo completar")

#Obteniendo Precios de los productos 
def ObteniendoPrecios():
    try:
        precios = driver.find_elements(By.CLASS_NAME,'base__price')
        for precio in precios:
            print(precio.text)
    except:
        print("No se pudo completar")

ObteniendoPrecios()