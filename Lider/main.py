import requests 
import json 

from bs4 import BeautifulSoup

def CategoriaDespensa():
    url = ('https://www.lider.cl/supermercado/category/Activaciones/Supermercado/Productos_Despensa?page=1&hitsPerPage=100')
    headers = {'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
    peticion = requests.get(url, headers=headers)
        
    if peticion.status_code == 200:
        print("se hizo la conexiòn de manera correcta")
        cambiarDato = peticion.text
        soup = BeautifulSoup(cambiarDato, 'html.parser')
        encontrarEtiqueta = soup.find('script', {'type':'application/ld+json'})
        #print(encontrarEtiqueta)
        textosinetiqueta = encontrarEtiqueta.string
        print(textosinetiqueta)
        with open ('LiderDespensa1.json', 'w') as f:
            json.dump(textosinetiqueta, f)
    else:
        print(f'erorr en la conexiòn {peticion.raise_for_status()}')

""" def CategoriaDespensa2():
    url = ('https://www.lider.cl/supermercado/category/Activaciones/Supermercado/Productos_Despensa?page=2&hitsPerPage=100')
    headers = {'user-agent' : 'Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41'}
    peticion = requests.get(url, headers=headers)
    
    if peticion.status_code == 200:
        print("se hizo la conexiòn de manera correcta")
        cambiarDato = peticion.text
        soup = BeautifulSoup(cambiarDato, 'html.parser')
        encontrarEtiqueta = soup.find('script', {'type':'application/ld+json'})
        #print(encontrarEtiqueta)
        textosinetiqueta = encontrarEtiqueta.string
        print(textosinetiqueta)
        with open ('LiderDespensa2.json', 'w') as f:
            json.dump(textosinetiqueta, f)
    else:
        print(f'erorr en la conexiòn {peticion.raise_for_status()}')

contador = 0 
while contador < 3:
    if contador == 1:
        CategoriaDespensa()
    
    elif contador == 2:
        CategoriaDespensa2()
    contador +=1

 """

CategoriaDespensa()