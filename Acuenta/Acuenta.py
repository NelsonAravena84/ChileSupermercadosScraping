from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


driver_location = '/usr/bin/chromedriver'
binary_location = '/usr/bin/google-chrome'

opts = webdriver.ChromeOptions()
Options.binary_location = binary_location

opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")

driver = webdriver.Chrome(
    service=Service(driver_location),
    options=opts
)

#PRODUCTOS DESPENSA 

ListaNombresDespensa = []
ListaPrecioDespensa = []

def CategoriaDespensa(mostrar):
    driver.get('https://acuenta.cl/ca/despensa/05')
    sleep(20)

    #Mostrar nombre de los productos 
    if mostrar == 'nombres':
        try:
            nombres = driver.find_elements(By.CLASS_NAME,'prod__name')
            for nombre in nombres:
                ListaNombresDespensa.append(nombre.text)
        except:
            print("No se pudo completar")
        #return ListaNombresDespensa
    
    #Mostrar precio de los productos
    elif mostrar == 'precios':
        try:
            precios = driver.find_elements(By.CLASS_NAME,'base__price')
            for precio in precios:
                ListaPrecioDespensa.append(precio.text)
        except:
            print("No se pudo completar")

#PRODUCTOS CARNES

ListaNombresCarnes = []
ListaPrecioCarnes = []

def CategoriaCarnes(mostrar):
    driver.get('https://acuenta.cl/ca/carnes-y-pescados/03?categories=Salchichas+y+parrilleros%7E%7EVacuno%7E%7ECerdo%7E%7EPollo%7E%7EHamburguesas+y+churrascos%7E%7ENuggets+y+apanados%7E%7EPavo')
    sleep(20)

    #Mostrar nombre de los productos 
    if mostrar == 'nombres':
        try:
            nombres = driver.find_elements(By.CLASS_NAME,'prod__name')
            for nombre in nombres:
                ListaNombresCarnes.append(nombre.text)
        except:
            print("No se pudo completar")
    
    #Mostrar precio de los productos
    elif mostrar == 'precios':
        try:
            precios = driver.find_elements(By.CLASS_NAME,'base__price')
            for precio in precios:
                ListaPrecioCarnes.append(precio.text)
        except:
            print("No se pudo completar")

#PRDOCUTOS PESCADOS

ListaNombresPescados = []
ListaPrecioPescados = []

def CategoriaPescados(mostrar):
    driver.get('https://acuenta.cl/ca/carnes-y-pescados/03?categories=Pescados+y+Mariscos+Congelados')
    sleep(20)

    #Mostrar nombre de los productos 
    if mostrar == 'nombres':
        try:
            nombres = driver.find_elements(By.CLASS_NAME,'prod__name')
            for nombre in nombres:
                ListaNombresPescados.append(nombre.text)
        except:
            print("No se pudo completar")
    
    #Mostrar precio de los productos
    elif mostrar == 'precios':
        try:
            precios = driver.find_elements(By.CLASS_NAME,'base__price')
            for precio in precios:
                ListaPrecioPescados.append(precio.text)
        except:
            print("No se pudo completar")

#PRODUCTOS FRESCOS Y LACTEOS

ListaNombresFrescos = []
ListaPrecioFrescos = []

def CategoriaFrescos(mostrar):
    driver.get('https://acuenta.cl/ca/frescos-y-lacteos/07')
    sleep(20)

    #Mostrar nombre de los productos 
    if mostrar == 'nombres':
        try:
            nombres = driver.find_elements(By.CLASS_NAME,'prod__name')
            for nombre in nombres:
                ListaNombresFrescos.append(nombre.text)
        except:
            print("No se pudo completar")
    
    #Mostrar precio de los productos
    elif mostrar == 'precios':
        try:
            precios = driver.find_elements(By.CLASS_NAME,'base__price')
            for precio in precios:
                ListaPrecioFrescos.append(precio.text)
        except:
            print("No se pudo completar")

#PRODUCTOS BEBIDAS Y LICORES

ListaNombresBebidas = []
ListaPrecioBebidas = []

def CategoriaBebidas(mostrar):
    driver.get('https://acuenta.cl/ca/bebidas-y-licores/02')
    sleep(20)

    #Mostrar nombre de los productos 
    if mostrar == 'nombres':
        try:
            nombres = driver.find_elements(By.CLASS_NAME,'prod__name')
            for nombre in nombres:
                ListaNombresBebidas.append(nombre.text)
        except:
            print("No se pudo completar")
    
    #Mostrar precio de los productos
    elif mostrar == 'precios':
        try:
            precios = driver.find_elements(By.CLASS_NAME,'base__price')
            for precio in precios:
                ListaPrecioBebidas.append(precio.text)
        except:
            print("No se pudo completar")

#PRODUCTOS ASEO Y LIMPIEZA

ListaNombresAseo = []
ListaPrecioAseo = []

def CategoriaLimpieza(mostrar):
    driver.get('https://acuenta.cl/ca/aseo-y-limpieza/11')
    sleep(20)

    #Mostrar nombre de los productos 
    if mostrar == 'nombres':
        try:
            nombres = driver.find_elements(By.CLASS_NAME,'prod__name')
            for nombre in nombres:
                ListaNombresAseo.append(nombre.text)
        except:
            print("No se pudo completar")
    
    #Mostrar precio de los productos
    elif mostrar == 'precios':
        try:
            precios = driver.find_elements(By.CLASS_NAME,'base__price')
            for precio in precios:
                ListaPrecioAseo.append(precio.text)
        except:
            print("No se pudo completar")


#PRODUCTOS FRUTAS Y VERDURAS

ListaNombresFrutas = []
ListaPrecioFrutas = []
def CategoriaFrutas(mostrar):
    driver.get('https://acuenta.cl/ca/frutas-y-verduras/06')
    sleep(20)

    #Mostrar nombre de los productos 
    if mostrar == 'nombres':
        try:
            nombres = driver.find_elements(By.CLASS_NAME,'prod__name')
            for nombre in nombres:
                ListaNombresFrutas.append(nombre.text)
        except:
            print("No se pudo completar")
    
    #Mostrar precio de los productos
    elif mostrar == 'precios':
        try:
            precios = driver.find_elements(By.CLASS_NAME,'base__price')
            for precio in precios:
                ListaPrecioFrutas.append(precio.text)
        except:
            print("No se pudo completar")


CategoriaCarnes('nombres')
CategoriaBebidas('nombres')
CategoriaFrutas('nombres')
CategoriaLimpieza('nombres')
CategoriaFrescos('nombres')
CategoriaPescados('nombres')
CategoriaDespensa('nombres')

CategoriaCarnes('precios')
CategoriaBebidas('precios')
CategoriaFrutas('precios')
CategoriaLimpieza('precios')
CategoriaFrescos('precios')
CategoriaPescados('precios')
CategoriaDespensa('precios')