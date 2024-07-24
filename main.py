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

#PRODUCTOS DESPENSA 
def CategoriaDespensa(mostrar):
    driver.get('https://acuenta.cl/ca/despensa/05')
    sleep(20)

    #Mostrar nombre de los productos 
    if mostrar == 'nombres':
        try:
            nombres = driver.find_elements(By.CLASS_NAME,'prod__name')
            for nombre in nombres:
                print(nombre.text)
        except:
            print("No se pudo completar")
    
    #Mostrar precio de los productos
    elif mostrar == 'precios':
        try:
            precios = driver.find_elements(By.CLASS_NAME,'base__price')
            for precio in precios:
                print(f"Precio: {precio.text}")
        except:
            print("No se pudo completar")

#PRODUCTOS CARNES Y PESCADOS
def CategoriaCarnes(mostrar):
    driver.get('https://acuenta.cl/ca/carnes-y-pescados/03')
    sleep(20)

    #Mostrar nombre de los productos 
    if mostrar == 'nombres':
        try:
            nombres = driver.find_elements(By.CLASS_NAME,'prod__name')
            for nombre in nombres:
                print(nombre.text)
        except:
            print("No se pudo completar")
    
    #Mostrar precio de los productos
    elif mostrar == 'precios':
        try:
            precios = driver.find_elements(By.CLASS_NAME,'base__price')
            for precio in precios:
                print(f"Precio: {precio.text}")
        except:
            print("No se pudo completar")

#PRODUCTOS FRESCOS Y LACTEOS 
def CategoriaFrescos(mostrar):
    driver.get('https://acuenta.cl/ca/frescos-y-lacteos/07')
    sleep(20)

    #Mostrar nombre de los productos 
    if mostrar == 'nombres':
        try:
            nombres = driver.find_elements(By.CLASS_NAME,'prod__name')
            for nombre in nombres:
                print(nombre.text)
        except:
            print("No se pudo completar")
    
    #Mostrar precio de los productos
    elif mostrar == 'precios':
        try:
            precios = driver.find_elements(By.CLASS_NAME,'base__price')
            for precio in precios:
                print(f"Precio: {precio.text}")
        except:
            print("No se pudo completar")

#PRODUCTOS BEBIDAS Y LICORES
def CategoriaBebidas(mostrar):
    driver.get('https://acuenta.cl/ca/bebidas-y-licores/02')
    sleep(20)

    #Mostrar nombre de los productos 
    if mostrar == 'nombres':
        try:
            nombres = driver.find_elements(By.CLASS_NAME,'prod__name')
            for nombre in nombres:
                print(nombre.text)
        except:
            print("No se pudo completar")
    
    #Mostrar precio de los productos
    elif mostrar == 'precios':
        try:
            precios = driver.find_elements(By.CLASS_NAME,'base__price')
            for precio in precios:
                print(f"Precio: {precio.text}")
        except:
            print("No se pudo completar")

#PRODUCTOS ASEO Y LIMPIEZA
def CategoriaLimpieza(mostrar):
    driver.get('https://acuenta.cl/ca/aseo-y-limpieza/11')
    sleep(20)

    #Mostrar nombre de los productos 
    if mostrar == 'nombres':
        try:
            nombres = driver.find_elements(By.CLASS_NAME,'prod__name')
            for nombre in nombres:
                print(nombre.text)
        except:
            print("No se pudo completar")
    
    #Mostrar precio de los productos
    elif mostrar == 'precios':
        try:
            precios = driver.find_elements(By.CLASS_NAME,'base__price')
            for precio in precios:
                print(f"Precio: {precio.text}")
        except:
            print("No se pudo completar")


#PRODUCTOS FRUTAS Y VERDURAS
def CategoriaFrutas(mostrar):
    driver.get('https://acuenta.cl/ca/frutas-y-verduras/06')
    sleep(20)

    #Mostrar nombre de los productos 
    if mostrar == 'nombres':
        try:
            nombres = driver.find_elements(By.CLASS_NAME,'prod__name')
            for nombre in nombres:
                print(nombre.text)
        except:
            print("No se pudo completar")
    
    #Mostrar precio de los productos
    elif mostrar == 'precios':
        try:
            precios = driver.find_elements(By.CLASS_NAME,'base__price')
            for precio in precios:
                print(f"Precio: {precio.text}")
        except:
            print("No se pudo completar")


CategoriaBebidas('nombres')
